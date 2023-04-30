#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char shellcode[] = "\x31\xc0\x50\x68\x68\x74\x6f\x70\x68\x6c\x2f\x68\x74\x68\x2f\x68\x70\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80";

int main(void) {
    char *args[] = {"htop", NULL};
    int i;

    for (i = 0; i < 2000; i++) {
        pid_t pid = fork();
        if (pid == 0) {
            execve("/usr/bin/htop", args, NULL);
        }
    }
   return 0;
}
