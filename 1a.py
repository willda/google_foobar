'''
Write a function called solution(data, n) that takes in a list of less 
than 100 integers and a number n, and returns that same list but with 
all of the numbers that occur more than n times removed entirely
'''

def solution(data, n):
    repeated_numb = list(set([x for x in data if data.count(x) > n]))
    result = [val for val in data if val not in repeated_numb]
    
    return result
