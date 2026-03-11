''' 
1. Write a python code for the factorial of a number ?
'''
n=int(input("enter n"))
fact=1
for _ in range(1, n+1):
    fact*=i
print(fact)
'''
2) write a python code to check whether a number is armstrong or not?
ex: 153-->1,5,3-->(1**3) + (3**3) = 153'''
num = int(input("Enter a number: "))
n = num
power = len(str(num))
total = 0

while n > 0:
    digit = n % 10
    total += digit ** power
    n //= 10

if total == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")



'''
3) write a python code to check whether a number is prime or not? 
'''
n=int(input())
flag=0
for i in range(2,n):
    if n%i==0:
        flag=1
        break
if flag==0:
    print("prime")
else:
    print("not prime")
'''
4) print the prime numbers with a range?
n=int(input())
for i in range(2,n):
    flag=0
    for j in range(2,i):
        if i%j==0:
            flag=1
            break
    if flag==0:
        print(i)


5) monotonic of an array ?
ex: 1,2,3,4,5 -->monotonic
5,4,3,2,1 -->monotonic
5,4,8,6,2,1 --> monotonic
10,5,6,25,45 --> not monotonic
'''n=int(input())
arr=list(map(int,input().split()))
is_increasing=True
is_decreasing=True
for i in range(1,n):
    if arr[i]>arr[i-1]:
        is_decreasing=False
    if arr[i]<arr[i-1]:
        is_increasing=False
if is_increasing or is_decreasing:
    print("monotonic")
else:
    print("not monotonic")
#palindrome number
n=int(input())
temp=n
rev=0
while temp>0:
    r=temp%10
    rev=rev*10+r
    temp=temp//10
if rev==n:
    print("palindrome")
else:
    print("not palindrome")

        
'''
#reverse of a integer with +ve and -ve number
n=int(input())
sign =1
if n<0:
    sign=-1
    n=-n
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
rev=rev*sign
if rev<-2**31 or rev>2**31-1:
    print(0)
else:
    print(rev)
#roman to integer
s=input().upper()
romans={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
total=0
for i in range(len(s)):
    if i>0 and romans[s[i]]>romans[s[i-1]]:
        total+=romans[s[i]]-2*romans[s[i-1]]
    else:
        total+=romans[s[i]]
print(total) 
'''

#happy numbers
n=int(input())
def is_happy(num):
    seen=set()
    while num!=1 and num not in seen:
        seen.add(num)
        num=sum(int(digit)**2 for digit in str(num))
    return num==1
if is_happy(n):
    print("happy")
else:    print("not happy")


