# Arithmetic Expression
'''
Consider an arithmetic expression of the form a#b=c. Check whether it is possible to replace # with one of the four signs: 
+, -, * or / to obtain a correct expression.
'''

# Example
'''
For a = 2, b = 3, and c = 5, the output should be solution(a, b, c) = true.

We can replace # with a + to obtain 2 + 3 = 5, so the answer is true.

For a = 8, b = 2, and c = 4, the output should be solution(a, b, c) = true.

We can replace # with a / to obtain 8 / 2 = 4, so the answer is true.

For a = 8, b = 3, and c = 2, the output should be solution(a, b, c) = false.

    8 + 3 = 11 ≠ 2;
    8 - 3 = 5 ≠ 2;
    8 * 3 = 24 ≠ 2;
    8 / 3 = 2.(6) ≠ 2.

So the answer is false.
'''

# Solution:

def solution(a, b, c):
    if a + b == c:
        return True
    elif a - b == c:
        return True
    elif a * b == c:
        return True
    elif a / b == c:
        return True
    else:
        return False

a = 2
b = 3
c = 5
print(solution(a, b, c))

a = 8
b = 2
c = 4
print(solution(a, b, c))

a = 8
b = 3
c = 2
print(solution(a, b, c))