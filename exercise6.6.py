def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]

def is_palindrome(string):
    new_string = str(string)
    if len(new_string) <= 1:
        return (True)
    elif first(new_string) == last(new_string):
        return is_palindrome(middle(new_string))
    else:
        return (False)

print(is_palindrome('worw'))
print(is_palindrome('woow'))
