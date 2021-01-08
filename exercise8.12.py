amount=1
string="abc-ABC"
for i in string:
    if ord(i)>=97 and ord(i)<=122:
        value=ord(i)+amount
        if value>122:
            print(chr(value-26),end="")
        else:
            print(chr(value),end="")
    elif ord(i)>=65 and ord(i)<=90:
        value = ord(i) + amount
        if value > 90:
            print(chr(value - 26),end="")
        else:
            print(chr(value),end="")
    else:
        print(i,end="")

