def count(word, letter):
    how_many = 0
    for char in word:
        if char == letter:
            how_many = how_many + 1
    print(how_many, "count version 1")

count('banana', 'a')