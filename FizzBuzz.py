"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.

answer[i] == "Fizz" if i is divisible by 3.

answer[i] == "Buzz" if i is divisible by 5.

answer[i] == i (as a string) if none of the above conditions are true.
"""

def fizzbuzz(n):
    result = []
    for i in range(1, n+1):
        # check if i is divisible by 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            result.append('FizzBuzz')
        # check if i is divisible by 3
        elif i % 3 == 0:
            result.append('Fizz')
        # check if i is divisible by 5
        elif i % 5 == 0:
            result.append('Buzz')
        # if i is not divisible by 3 or 5
        else:
            result.append(str(i))

    return result

# Test function with test cases
test1 = fizzbuzz(3)
test2 = fizzbuzz(5)
test3 = fizzbuzz(15)

print(test1)
print(test2)
print(test3)
