# Extra Number
'''
You're given three integers, a, b and c. It is guaranteed that two of these integers are equal to each other. 
What is the value of the third integer?
'''

# Example
'''
For a = 2, b = 7, and c = 2, the output should be solution(a, b, c) = 7.

The two equal numbers are a and c. The third number (b) equals 7, which is the answer.
'''

# Solution:

def solution(a, b, c):
    if a == b:
        return c
    elif a == c:
        return b
    else:
        return a

a = 2
b = 7
c = 2
print(solution(a, b, c))