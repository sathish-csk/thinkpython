import sys
import os

def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return False

if __name__ == '__main__':
    print(find('foo fighters rock', 'i', 6))
    print('foo fighters rock'[5])
