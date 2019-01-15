#!/usr/bin/python
from Crypto.Cipher import AES 


p = 9605179
g = 15
A = 8706295
B = 4045784

a = 1 
b = 2 
while (pow(g,a,p) != A):
    a+=1

while (pow (g,b,p) != B):
    b+=1
    

key = pow (A,b,p)


flag="f9a385a21faa40ae6313d225987b87c554ca0a2e32a42a28a71c1c155ec787d76a4ea9aeb71339335747b91bd50faa99"
key = str(key)
while len(key) < 32:
	key = '0'+key
print key
todo = AES.new(key, AES.MODE_ECB)
cipher = todo.decrypt(flag)

print cipher

cipher = cipher.decode('hex')

