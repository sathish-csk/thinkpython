import sys
import os

def eval_loop():
    while True:
        user_string = input('>>> ')
        if user_string == 'done':
            break
        else:
            print(user_string)
            result = eval(user_string)
            print(result)

if __name__ == '__main__':
    eval_loop()