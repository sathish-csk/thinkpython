import sys
import os

def is_power(a,b):
    if (a % b == 0):
        return True
        if (a/b == 1):
            return True
        else:
            (is_power (a/b, b) )
    else:
        return False

if __name__ == '__main__':
    print(is_power(64,2))
    print(is_power(9,2))
    