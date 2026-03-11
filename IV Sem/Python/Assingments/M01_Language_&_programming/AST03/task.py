def Student_Grade_System(name:str,n1: int,n2: int,n3: int) -> str:
    average = (n1 + n2 + n3) / 3
    if average >= 50:
        return f"{name} has passed with an average of {average:.2f}"
    else:
        return f"{name} has failed with an average of {average:.2f}"
if __name__ == '__main__':
    name = input()
    n1,n2,n3 = list(map(int,input().split()))
    print(Student_Grade_System(name,n1,n2,n3))
    