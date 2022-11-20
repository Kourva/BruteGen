#!/usr/bin/env python3

import random
import time
import sys

words = "ab!cd@0efg9#hi8$jklm%7n6^opq&-_=+'\"r4*9st5uv(3wx)2yz1"
red = "\033[1;31m"
res = "\033[m"
blu = "\033[1;32m"
whi = "\033[1;37m"
for char in (f"{blu}Enter any key to start BruteForce..."):
	sys.stdout.write(char)
	sys.stdout.flush()
	time.sleep(0.01)
input()

for i in range(100000):
    progress = int(i/100000*100) + 1
    text = f"\r{red}[{whi}%{str(progress).ljust(3)}{red}]{whi} ; {blu}{str(i+1).rjust(6)}{whi}/100000   ->   {red}{''.join(random.choices(words,k=20))}{res}"
    sys.stdout.write(text)
    sys.stdout.flush()
    # time.sleep(.03)

print() 
