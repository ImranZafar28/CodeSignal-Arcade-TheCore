# Is Infinite Process?
'''
Given integers a and b, determine whether the following pseudocode results in an infinite loop

while a is not equal to b do
    increase a by 1
    decrease b by 1

Assume that the program is executed on a virtual machine which can store arbitrary long numbers and execute forever.
'''

# Example
'''
For a = 2 and b = 6, the output should be solution(a, b) = false;

For a = 2 and b = 3, the output should be solution(a, b) = true.
'''

# Solution:

def solution(a, b):
    while a <= b:
        if a == b:
            return False
        else:
            a += 1
            b -= 1
    return True

a = 2
b = 6
print(solution(a, b))

a = 2
b = 3
print(solution(a, b))