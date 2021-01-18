file=open('words.txt')
string = file.readline()
list=string.strip().split(" ")

for i in list:
    if len(i)>20:
        print(i)