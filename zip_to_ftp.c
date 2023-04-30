#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <dirent.h>

int main(int argc, char *argv[]) {

    if (argc != 4) {
        printf("Usage: %s <path_to_folder> <ftp_server> <ftp_credentials>\n", argv[0]);
        return 1;
    }

    char *zip_cmd = "zip -r /tmp/UserData.zip "; // Path or folder to compress
    char *user_folder = argv[1];
    char *zip_args = strcat(zip_cmd, user_folder);
    system(zip_args);

    char *ftp_cmd = "curl -T /tmp/UserData.zip ftp://";
    char *ftp_server = argv[2];
    char *ftp_credentials = argv[3];
    char *ftp_args = strcat(ftp_cmd, ftp_server);
    ftp_args = strcat(ftp_args, "/");
    ftp_args = strcat(ftp_args, ftp_credentials);
    system(ftp_args);

    remove("/tmp/UserData.zip");

    return 0;
}
