def check_fermat(a,b,c,n):
    if a**n + b ** n == c**n:
        print('Holy smokes, Fermat was wrong!')
    else:
        print("No,that doesn't work.")

a = int(input('please input the value of a\n'))
b = int(input('please input the value of b\n'))
c = int(input('please input the value of c\n'))
n = int(input('please input the value of n\n'))
print('a =',a,'b =',b,'c =',c)
check_fermat(a,b,c,n)