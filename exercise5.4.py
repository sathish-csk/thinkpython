def is_triangle(a,b,c):
    if a + b >= c and a+c >= b and b+c >= a:
        print("Yes")
    else:
        print("No")

a = int(input('please input the value of a'))
b = int(input('please input the value of b'))
c = int(input('please input the value of c'))
print("a = ",a,'b = ',b,'c = ',c)

is_triangle(a,b,c)