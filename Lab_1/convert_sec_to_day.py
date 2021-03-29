'''
write a python program to convert second to day, hour,minutes and sec
'''
sec=int(input("Enter the seconds"))
min=(sec//60)
hrs=((sec//60)//60)
day=(((sec//60)//60)//24)

print(f"Day {day} Day {hrs} Hour {min} Mins {sec} sec")76543