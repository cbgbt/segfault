import ctypes
import sys


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


class Segfault(RuntimeError):
    pass


def handle_segfault_exception(exctype, value, trace):
    if isinstance(value, Segfault):
        segfault()
    else:
        sys_exc_hook(exctype, value, trace)

sys_exc_hook = sys.excepthook
sys.excepthook = handle_segfault_exception
