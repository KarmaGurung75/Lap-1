'''
write a python program to sum of three given integers. however, if two values are equal sum will be zero
'''
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
num3=int(input("Enter the third number"))
if num1==num2 or num2==num3 or num3==num1:
    print("the sum is zero")
else:
    sum = num1 + num2 + num3
    print(f"the sum is {sum}")