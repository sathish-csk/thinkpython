letter="d"
word="PEtCskedmi"
word_list=list(word)
n=2
s=[]
sentence=""
s.append("csk")
s.append("mi")

for i in range(n):
    if word.lower().find(s[i]):
        value=word.lower().find(s[i])
        for k in range(value,value+len(s[i])):
            if word[k].islower():
                if word[k].lower()==letter:
                    print(word_list[k])
                else:
                    word_list[k]=letter.lower()
            else:
                if word[k].lower()==letter:
                    word_list[k]='a'
                else:
                    word_list[k]=letter.upper()
for i in word_list:
    sentence+=i
print(sentence)




