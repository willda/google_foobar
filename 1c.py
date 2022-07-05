'''
Given a minion ID as a string n representing a nonnegative 
integer of length k in base b, where 2 <= k <= 9 and 
2 <= b <= 10, write a function solution(n, b) which returns 
the length of the ending cycle of the algorithm above starting with n.
'''

def to_base(n, base):
    table = "0123456789"
    if n < base:
        return table[n]
    else:
        return to_base(n // base, base) + table[n % base]

def solution(n,b):
    iterations = 0
    z = None
    hist = {n: 0}

    while n != 0:
        iterations += 1
        x = ''.join(sorted(n, reverse = True))
        y = ''.join(sorted(n))
        z = int(x, b) - int(y, b)
        z = to_base(z, b).zfill(len(n))

        if z in hist:
            return iterations - hist[z]
        
        hist[z] = iterations
        n = z

    return 1
