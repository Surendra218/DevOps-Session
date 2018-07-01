#!/usr/bin/python

from random import randint

import os

for rang_int in range(5):
 random_int = randint(0,100)
 os.system("touch %s-%s.txt" %(rang_int,random_int))
