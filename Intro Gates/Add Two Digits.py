# Add Two Digits
'''
You are given a two-digit integer n. Return the sum of its digits.
'''

# Example
'''
For n = 29, the output should be solution(n) = 11.
'''

# Solution:

def solution(n):
    s = str(n)
    return int(s[0]) + int(s[1])

print(solution(29))