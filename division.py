def division(num1, num2):
    if num2 == 0:
        print("you can't divide by zero")
    else:
        return num1/num2


n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
print(f"the division of {n1} / {n2} = {division(n1,n2)}")
