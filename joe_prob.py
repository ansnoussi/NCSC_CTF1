#!/usr/bin/python
from math import *
from pwn import *

s = remote("34.247.111.169",4010)
data = s.recv(1024)
data = s.recv(1024)

num = data.split("persons")[0].split("are")[1].strip
n = int(num)
print num
w = 2*(n-pow(2,math.floor(math.log(n)/math.log(2))))+1
print w
s.sendline(str(int(w)))
print s.recv(1024)
