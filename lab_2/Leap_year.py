'''
Check wether the given year is leap year or not. If year is leap print 'Lepa Year' else print 'Common Year'.
Hint:   a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100.
        a year is always a leap year if its number is exactly divisible by 400
'''

day=int(input('Enter the year'))
if day%4==0:
    print("It is Leap year")
else:
    print("It is common year")