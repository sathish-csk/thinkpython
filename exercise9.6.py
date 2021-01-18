def is_abecdarian(s):
    index = 0
    while index < len(s)-1:
        if ord(s[index + 1]) == ord(s[index])+1:
            return True
        index += 1
    return False
line="Here is the abcdrian words abcd in the sentence"
words=line.split(" ")
count = 0
for word in words:
    print(is_abecdarian(word))
