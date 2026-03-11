'''
+Set:
1.use{} to create a set
2.duplicate elements are not allowed
3.set unindexed and unordered
4. set is mutable.

s={1,True,3.14,"Hello",1,2,3}
print(s,type(s))
print(s[3])

#Adding elements to a set
A={1, 2, 3}
B={3,4, 5}
A.add(7)
B.update({6,7})
print(A,B)

#Removing elements from a set
A.pop()
print(A)
A.remove(2)
print(A)

#268:Missing Number
def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
print(missing_number([3, 0, 1]))

# 349.Intersection of Two Arrays
def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return list(set1.intersection(set2))
print(intersection([1, 2, 2, 1], [2, 2]))


t = (10,23,50,12,45,32,48)
t2 = ("sai","kalyani","krishna")

print(t[0])
print(t[-1])
print(t + t2)
print(t,t2)
print(t[1:4])
print(t[:5])
print(t[:-1])

#349.Intersection of Two Arrays
def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return list(set1.intersection(set2))
print(intersection([1, 2, 2, 1], [2, 2]))

#657 Robot Return to Origin
def judge_circle(moves):
    x = 0
    y = 0
    for move in moves:
        if move == 'U':
            y += 1
        elif move == 'D':
            y -= 1
        elif move == 'L':
            x -= 1
        elif move == 'R':
            x += 1
    return x == 0 and y == 0
'''
#1 Two Sum
def two_sum(nums, target): 
    num_to_index = {}  
    for i, num in enumerate(nums):  
        complement = target - num  
        if complement in num_to_index:  
            return [num_to_index[complement], i]  
        num_to_index[num] = i  
    return []


