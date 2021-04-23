#!/bin/python3

import math
import os
from random import randint
import re
import sys

if __name__ == '__main__':
    for i in range (0, 100):
        n = randint(1 , 100)
        
        #n = int(input().strip())
        if(n%2 or 6 <= n <= 20):
            #print(n)
            print("Not Weird")
            #pass
        else:
            #print(i,n)
            print(i,"Weird")
        
