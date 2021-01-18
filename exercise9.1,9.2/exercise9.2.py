fin=open('words.txt')
word=fin.readline()
for i in word:
    if not 'e' in i:
        print(True)
    print(False)



