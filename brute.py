#!/usr/bin/python

import hashlib
alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
sta = "securinets"
# print hashlib.md5(ch).hexdigest()
# 55f4b1867f59b3d928893496bb9ce320
s="securinets"



for i in alpha:
    for j in alpha:
        for k in alpha:
            for l in alpha:
                x = s+i+j+k+l
                if (hashlib.md5(x).hexdigest() == "55f4b1867f59b3d928893496bb9ce320"):
                    print x
                    exit(0)
                    
 
