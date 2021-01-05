import sys
import os


def find(word, letter, start):
    if start:
        index = start
    else:
        index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

if __name__ == '__main__':
    print(find('foo fighters rock', 'i', 6))
    print('foo fighters rock'[5])