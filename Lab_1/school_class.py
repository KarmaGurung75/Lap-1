'''
A school decided to replace the desk in three classroom. Each desk sits two students.
given the number of student in each class,print the smallest possible number of desks that can be purchased.
the program should read three integers: The number of the students in each of the three classes,a,b and c respectively.
in the first test there are three groups. the first group hs 20 students and thus need 10 desks.
the second group has 21 student, so they can get by with no fewer  than 11 desks.
11 desk are also enough for the third group of 22 students. So, we need 32 desk in total.
'''
class_a=int(input("Enter the number of the student that can in class A:\n"))
class_b=int(input("Enter the number of the student that can be in class B:\n"))
class_c=int(input("Enter the number of the student that can be in class C:\n"))
desk_a=class_a//2
print(desk_a,"Desk is needed in class A")
desk_b=class_b//2
print(desk_b,"Desk is needed in class B")
desk_c=class_c//2
print(desk_c,"Desk is needed in class C")
remain_a=class_a%2
print(remain_a,"is the remaining desk")
remain_b=class_b%2
print(remain_b,"is the remaining desk")
remain_c=class_c%2
print(remain_c,"is the remaining desk")
total_desk=desk_a + desk_b + desk_c + remain_a + remain_b + remain_c
print(total_desk,"desk is needed in total")