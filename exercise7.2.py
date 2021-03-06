def square_root(a):
    # we will guess that x will be 1/2 of a, to start
    x =  0.75 * float(a)
    epsilon = 0.000001
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y
    return x
    

if __name__ == '__main__':
    print square_root(144)
    print square_root(121)