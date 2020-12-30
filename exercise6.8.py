def gcd(a,b):
    # catch base case from the door
    if b == 0:
        return a
    # otherwise, do the other steps
    else:
        # compute remainder
        remainder = a % b
        # If we have base case, no need to
        # call again
        if remainder == 0:
            return b
        # otherwise, we recurse and grab the return value
        else:
            return gcd(b, remainder)


if __name__ == '__main__':
    print(gcd(60, 80))
    print(gcd(15, 12))
    print(gcd(24,8))