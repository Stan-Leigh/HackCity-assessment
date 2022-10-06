"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""

def runningsum(nums):
    # create list to store the result
    result = []
    # create a variable to keep track of the running sum
    counter = 0

    for i in nums:
        # add each input value to the counter
        counter += i
        # append the current running sum to the result list
        result.append(counter)

    return result

# Test function with test cases
test1 = runningsum([1, 2, 3, 4])
test2 = runningsum([1, 1, 1, 1, 1])

print(test1)
print(test2)
