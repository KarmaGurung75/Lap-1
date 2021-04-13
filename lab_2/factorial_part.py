'''
7. Given the positive real number print its fractional part
'''

import math
num=int(input("Enter the number"))
a=math.modf(num)
print(f"{a}")