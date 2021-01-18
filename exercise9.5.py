def uses_all(word, use_all_chars):
    for char in use_all_chars:
        if char.lower() not in word.lower():
            if char != " ":  # ignore space character
                return False
    return True

print(uses_all("Ho lo ho","acefhlo"))