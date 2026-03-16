'''
#Reverse array using
#1. Slicing 
arr=list(map(int,input().split()))
print(arr[::-1])
#2.using reversed() function
arr=list(map(int,input().split()))
print(list(reversed(arr)))
#3. using for loop
arr=list(map(int,input().split()))
reversed_arr=[]
for i in range(len(arr)-1,-1,-1):
    reversed_arr.append(arr[i])
print(reversed_arr)

#3) Find min and max ele?
#4)Find Second largest element?
#5)Remove Duplicates from array?
#find max and  in ele?
arr=list(map(int,input().split()))
print("Max:",max(arr))
print("Min:",min(arr))

#find second largest element
arr=list(map(int,input().split()))
arr.sort()
print("Second Largest:",arr[-2])
#remove duplicates from array
arr=list(map(int,input().split()))
print(list(set(arr)))

#6)Count the frequency of each elements
arr=list(map(int,input().split()))
frequency={}    
for i in arr:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
print(frequency)

#7) Rotate Array
def rotate_array(arr, k):
    k = k % len(arr)  # Handle cases where k is greater than array length
    return arr[-k:] + arr[:-k]
arr=list(map(int,input().split()))
k=int(input("Enter number of positions to rotate: "))  
print(rotate_array(arr, k))
 '''

 #724. Find Pivot Index
def pivot_index(nums):
    total_sum = sum(nums)
    left_sum = 0
    for i, num in enumerate(nums):
        if left_sum == (total_sum - left_sum - num):
            return i
        left_sum += num
    return -1
print(pivot_index([1, 7, 3, 6, 5, 6]))
