#!/usr/bin/env python3

print("Credits to: ZylonAU")

from pwn import *
import re

p = remote("word-search.ctf.fifthdoma.in",4243)

# Brute force solution
tiles = 15
for x in range(tiles):
        for y in range(tiles):
                for x1 in range(tiles):
                        for y1 in range(tiles):
                                # Only send valid guesses
                                if x == x1 or y == y1 or abs(x1 - x) == abs(y1 - y):
                                        p.sendline(f'{x},{y}'.encode())
                                        p.sendline(f'{x1},{y1}'.encode())
response = str(p.recvall(timeout=1))
flag = re.search('FLAG{[A-Za-z0-9_]*}', response)
print(flag.group())
