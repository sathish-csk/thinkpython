f = open("words.txt", "r")
words=f.read()
for i in words.split():
	print(i)
