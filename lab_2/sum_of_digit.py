'''
8. given a three-digit number. Find the sum of its digit
'''
def getSum(n):
    sum = 0
    while (n != 0):
        sum = sum + int(n % 10)
        n = int(n / 10)
    return sum
n = 687
print(getSum(n))