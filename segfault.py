import ctypes


POINTER_SKIP_INTERVAL = 256


# Borrowed from https://wiki.python.org/moin/CrashingPython
def segfault():
    """Segfault the Python interpeter"""
    mem = ctypes.c_int8(0)
    pointer = ctypes.pointer(mem)
    ndx = 0
    while True:
        pointer[ndx] = 0
        ndx += POINTER_SKIP_INTERVAL
