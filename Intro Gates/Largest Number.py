# Largest Number
'''
Given an integer n, return the largest number that contains exactly n digits.
'''

# Example
'''
For n = 2, the output should be solution(n) = 99.
'''

# Solution:

def solution(n):
    num = ''
    for i in range(n):
        num += '9'
    return int(num)

print(solution(2))