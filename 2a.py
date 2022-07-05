'''
You need to know how many replication cycles (generations) 
it will take to generate the correct amount of bombs to destroy 
the LAMBCHOP. Write a function solution(M, F) where M and F are 
the number of Mach and Facula bombs needed. Return the fewest number 
of generations (as a string) that need to pass before you'll have 
the exact number of bombs necessary to destroy the LAMBCHOP, or the 
string "impossible" if this can't be done! 
'''

def solution(x, y):
    count = 0
    x = int(x)
    y = int(y)

    while x != y:
        if x > 1 and y > 1:
            if x > y:
                count += x//y
                x = x - y * (x//y)
            elif x < y:
                count += y//x
                y = y - x * (y//x)
                
        elif x != 0 and y != 0:
            if x > y:
                count += x - y
                x = 1
                break
            elif x < y:
                count += y - x
                y = 1
                break
        else:
            break
        
    if x == 1 and y == 1 and count != 0:
        return str(count)
    else:
        return "impossible"
