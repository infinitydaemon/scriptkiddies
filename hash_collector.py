import ctypes
import sys

SYS_read = 0
SYS_write = 1
SYS_open = 2
SYS_close = 3
SYS_mmap = 9
PROT_READ = 1
MAP_PRIVATE = 2

class iovec(ctypes.Structure):
    _fields_ = [("iov_base", ctypes.c_void_p), ("iov_len", ctypes.c_size_t)]

class ucred(ctypes.Structure):
    _fields_ = [("pid", ctypes.c_int), ("uid", ctypes.c_int), ("gid", ctypes.c_int)]

class msghdr(ctypes.Structure):
    _fields_ = [
        ("msg_name", ctypes.c_void_p),
        ("msg_namelen", ctypes.c_uint),
        ("msg_iov", ctypes.POINTER(iovec)),
        ("msg_iovlen", ctypes.c_size_t),
        ("msg_control", ctypes.c_void_p),
        ("msg_controllen", ctypes.c_size_t),
        ("msg_flags", ctypes.c_int),
    ]

class mmsghdr(ctypes.Structure):
    _fields_ = [("msg_hdr", msghdr), ("msg_len", ctypes.c_uint)]

libc = ctypes.CDLL("libc.so.6")
syscall = libc.syscall
recvmsg = libc.recvmsg
munmap = libc.munmap

def collect_kernel_hashes():

    fd = syscall(SYS_open, "/dev/kmem", 0)
    if fd < 0:
        print("Failed to open /dev/kmem")
        return

    msg = msghdr()
    iovec_buffer = ctypes.create_string_buffer(0x1000)
    msg.msg_iov = ctypes.pointer(iovec(ctypes.addressof(iovec_buffer), 0x1000))
    msg.msg_iovlen = 1
    recvmsg(fd, ctypes.pointer(msg), 0)
    hashes = []
    data = ctypes.string_at(iovec_buffer, 0x1000)
    syscall(SYS_close, fd)
    munmap(iovec_buffer, 0x1000)

    return hashes

extracted_hashes = collect_kernel_hashes()
print(extracted_hashes) 
