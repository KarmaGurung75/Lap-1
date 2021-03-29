'''
2.WAP which accepts marks of four subjects and display toatal marks, percentage and grade.
Hint: more than 70%-->distinction, morethan 60% ---> first, more than 40% --> pass
'''
eng=int(input("Enter the marks of English subject "))
nepali=int(input("Enter the marks of nepali subject "))
math=int(input("Entet the marks of Math subject "))
acc=int(input("Enter the marks of Account subject "))
total=eng+nepali+math+acc
total_per=total/400*100
if total_per>70:
    print("Congrate  for scoring distinction")
elif total_per>=60:
    print("You have score First division")
elif total_per>=40:
    print("You have pass")
else:
    print("you have fail")