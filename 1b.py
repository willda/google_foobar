'''
Given a non-empty list of positive integers l and a target 
positive integer t, write a function solution(l, t) which 
verifies if there is at least one consecutive sequence of 
positive integers within the list l (i.e. a contiguous sub-list) 
that can be summed up to the given target positive integer 
t (the key) and returns the lexicographically smallest list 
containing the smallest start and end indexes where this 
sequence can be found, or returns the array [-1, -1] in 
the case that there is no such sequence (to throw off Lambda's 
spies, not all number broadcasts will contain a coded message).
'''

def solution(l, t):
    for start in range(0, len(l)):
        count = t
        for end in range(start, len(l)):
            count -= l[end]        
            if count < 0:
                break
            elif count == 0:
                return(start, end)
    return(-1)
