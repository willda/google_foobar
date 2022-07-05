'''
Write a function solution(h, q) - where h is the height 
of the perfect tree of converters and q is a list of positive 
integers representing different flux converters - which returns 
a list of integers p where each element in p is the label of 
the converter that sits on top of the respective converter in 
q, or -1 if there is no such converter.  
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
