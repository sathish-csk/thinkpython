def is_palindrome(word):
    return word == word[::-1]

if __name__ == '__main__':
    print(is_palindrome('bob'))
    print(is_palindrome('alpapla'))
    print(is_palindrome('shlomo'))