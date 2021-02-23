'''N student take k apple and distribute them among each other evenly.
 the remainning (the undivisiable) part remains in the basker. The program read the number N and K.
 it should print the two answer for the above question
'''
stu=int(input("Enter the number of the student:"))
app=int(input("Enter the number of the apple:"))
div=(app/stu)
remain=(app%stu)
print("Each studemt got ",div)
print("The remainning apple ",remain)