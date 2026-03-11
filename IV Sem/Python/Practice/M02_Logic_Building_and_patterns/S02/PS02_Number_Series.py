#Number series : Sequential order of number in a particular pattterns 
'''1)Print n natural numbers ?

n=int(input("Enter a number:"))
for i in range(1,n+1):
    print(i)

2)Print n even numbers?
n=int(input("enter a number":))
for i in range(2,n+1,2):
    print(i)

3)Print n odd numbers?
n=int(input("enter a number":))
for i in range(1,n+1,2):
    print(i)


4)Print n Fibonacci numbers? 0,1,2,3,5,8,13,21,34...
n=int(input())
a=0
b=1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c 


5)Print the multiplication table of a given number?

n=int(input())
for i in range(1,11):
    print(n,"*",i,"=",n*i)

6)print the square of first n natural number?
'''
n=int(input())
for i in range(n+1,1):
    print(i*i,end=" ")
    





