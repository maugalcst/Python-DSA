'''
Note: a and b are not ordered!

Examples (a, b) --> output (explanation)
(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
Your function should only return a number, not the explanation about how you get that number.
'''

def get_sum(a,b):
    min = 0
    max = 0
    sum = 0
    
    if a >= b: 
        min = b
        max = a
    else: 
        min = a 
        max = b
        
    for i in range(min,max +1):
        sum += i
    return sum

'''
Best practices:

def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))
    
'''


        