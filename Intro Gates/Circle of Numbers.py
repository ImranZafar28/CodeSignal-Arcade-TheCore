# Circle of Numbers
'''
Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between 
any two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).

Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.
'''

# Example
'''
For n = 10 and firstNumber = 2, 
the output should be solution(n, firstNumber) = 7.
'''

# Solution:

def solution(n, firstNumber):
    d = n // 2
    return firstNumber + d if firstNumber < d else firstNumber - d

n = 10
firstNumber = 2
print(solution(n, firstNumber))