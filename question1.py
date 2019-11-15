#Write a program which takes 5 inputs from user for different subject’s
#marks, total it and generate mark sheet using grades ?



sub1 = int(input("Enter first subject marks: "))
sub2 = int(input("Enter Second subject marks: "))
sub3 = int(input("Enter third subject marks: "))
sub4 = int(input("Enter fourth subject marks: "))
sub5 = int(input("Enter fifth subject marks: "))

avg =  (sub1 + sub2 + sub3 + sub4+ sub5) / 5

if(avg>=90):
    print("A+")
elif(avg>=80 and avg<90):
    print("A")
elif(avg>=70 and  avg<80):
    print("B")
elif(avg>=60 and avg<70):
    print("C")
else:
    print("Fail")