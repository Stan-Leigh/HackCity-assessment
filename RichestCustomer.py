"""
You are given an m x n integer grid account where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

 A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

  Example 1:

Input: accounts = [[1,2,3],[3,2,1]]

Output: 6

Explanation:

1st customer has wealth = 1 + 2 + 3 = 6

2nd customer has wealth = 3 + 2 + 1 = 6

Both customers are considered the richest with a wealth of 6 each, so return 6.

 Example 2:

Input: accounts = [[1,5],[7,3],[3,5]]

Output: 10

Explanation:

1st customer has wealth = 6

2nd customer has wealth = 10

3rd customer has wealth = 8

The 2nd customer is the richest with a wealth of 10.

 Example 3:

Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]

Output: 17
"""

def richest_customer(accounts):
    # set variable for the wealth of the richest customer
    wealth = 0
    # loop through each customer
    for customer in accounts:
        # add the wealth in all the accounts
        customer_wealth = sum(customer)
        # set value to wealth if it is greater than the current wealth
        if customer_wealth > wealth:
            wealth = customer_wealth

    return wealth

# Test function with test cases
test1 = richest_customer([[1,2,3],[3,2,1]])
test2 = richest_customer([[1,5],[7,3],[3,5]])
test3 = richest_customer([[2,8,7],[7,1,3],[1,9,5]])

print(test1)
print(test2)
print(test3)
