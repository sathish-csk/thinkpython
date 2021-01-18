word="ccnssmkk"
i = 0
count = 0
while i < len(word)-1:
    if word[i] == word[i+1]:
        count = count + 1
        i = i + 2
    else:
        count = 0
        i = i + 1
if count == 3:
    print(count,end=" -> ")
    print(word)
else:
    print(f"{word} is not a triple double word.")
