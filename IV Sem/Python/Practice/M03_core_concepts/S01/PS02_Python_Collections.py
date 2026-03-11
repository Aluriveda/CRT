'''
# Running Sum of 1 D Array
def running_sum(numbers):
    total = 0
    result = []
    for num in numbers:
        total += num
        result.append(total)
    return result

print(running_sum([1, 2, 3, 4]))
'''

'''
nums = [1, 2, 3, 4]
result = []
s = 0
for ele in nums:
    s + ele
    result.append(s)
print(result)

ans = []
for i in range(len(nums)+1):
    ans.append(sum(nums[:i]))
print(ans)


#217. Contains Duplicate
def contains_duplicate(nums):  
    seen = set()  
    for num in nums:  
        if num in seen:  
            return True  
        seen.add(num)  
    return False
'''
#1672. Richest Customer Wealth
def maximum_wealth(accounts):
    max_wealth = 0
    for customer in accounts:
        wealth = sum(customer)
        max_wealth = max(max_wealth, wealth)
    return max_wealth
print(maximum_wealth([[1, 2, 3], [3, 4, 1]]))