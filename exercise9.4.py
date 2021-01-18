def uses_only(word, only_chars):
    for char in word:
        if char.lower() not in only_chars.lower():
            if char != " ":  # ignore space character
                return False
    return True
print(uses_only("fh fh fh", "acefh lo"))
