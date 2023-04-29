#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

#define BUFLEN 512  // max buffer lenght
#define PORT 53     // the port itself

int main(void)
{
    struct sockaddr_in si_me, si_other;
    int s, i, slen = sizeof(si_other), recv_len;
    char buf[BUFLEN];
     
    // create udp socket
    if ((s = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)) == -1)
    {
        printf("Failed to create socket\n");
        return 1;
    }
     
    // prepare socket struct
    memset((char *)&si_me, 0, sizeof(si_me));
    si_me.sin_family = AF_INET;
    si_me.sin_port = htons(PORT);
    si_me.sin_addr.s_addr = htonl(INADDR_ANY);
     
    // Bind to port
    if (bind(s, (struct sockaddr *)&si_me, sizeof(si_me)) == -1)
    {
        printf("Failed to bind socket\n");
        return 1;
    }
     
    // Keep listening for data
    while(1)
    {
        printf("Waiting for data...\n");
        fflush(stdout);
         
        // Receive data
        if ((recv_len = recvfrom(s, buf, BUFLEN, 0, (struct sockaddr *)&si_other, &slen)) == -1)
        {
            printf("Failed to receive data\n");
            return 1;
        }
         
        printf("Received packet from %s:%d\n", inet_ntoa(si_other.sin_addr), ntohs(si_other.sin_port));
        printf("Data: %s\n" , buf);

        char reply[BUFLEN] = {0};
        strncpy(reply, buf, recv_len);
        reply[2] |= 0x80; 
        reply[3] |= 0x80;
        sendto(s, reply, recv_len, 0, (struct sockaddr *)&si_other, slen);
    }
     
    close(s);
    return 0;
}
