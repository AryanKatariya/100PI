def autoNumber(n):
    s = pow(n,2)
    m = pow(10, len(str(n)))
    if (s % m == n):
        print("It's an Automorphic Number")
    else:
        print("It's not an Automorphic Number")
        
autoNumber(376)
autoNumber(377)
