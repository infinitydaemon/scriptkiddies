section .data
    script_name db "/path/to/shell.py",0

section .text
    global _start

_start:
    mov rax, 2           ; System call number for 'open'
    mov rdi, script_name ; Address of the script name
    mov rsi, 0           ; Open read-only
    mov rdx, 0           ; Default permissions
    syscall
    mov rbx, rax
    mov rax, 0           ; System call number for 'read'
    mov rdi, rbx         ; File descriptor
    mov rsi, rsp         ; Address of the buffer
    mov rdx, 4096        ; Read up to 4096 bytes
    syscall
    mov byte [rsp + rax], 0
    mov rax, 3           ; System call number for 'close'
    mov rdi, rbx         ; File descriptor
    syscall

    ; init the py interpreter
    mov rax, 0x3b        ; System call number for 'execve'
    mov rdi, script_name ; Address of the script name
    lea rsi, [rsp]       ; Address of the command-line arguments
    xor rdx, rdx         ; No environment variables
    syscall
    ; exit the interpreter value after return
    mov rax, 60          ; System call number for 'exit'
    xor rdi, rdi         ; Use the interpreter's return value
    syscall
