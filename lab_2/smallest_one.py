'''
4. Given three integer number, print the smallest one.
'''
num1=int(input('Enter the first number'))
num2=int(input('Enter the second number'))
num3=int(input('Enter the third number'))

if num1<num2 & num2<num3:
    print(f"{num1} is the smallest")
elif num2<=num1 & num1<=num3:
    print(f"{num2} is smallest")
else:
    print(f"{Num3} is smallest")