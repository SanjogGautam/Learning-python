'''5. WAP to input marks in 5 subjects and then calculate total marks, percentage, division and result(pass/fail).'''
def total_marks(s1,s2,s3,s4,s5):
    return s1+s2+s3+s4+s5
def percentage(total):
    return (total/500)*100
def division(perc):
    if perc<=100 and perc>90:
        return "A+"
    elif perc<=90 and perc>80:
        return "A"
    elif perc<=80 and perc>70:
        return "B+"
    elif perc<=70 and perc>60:
        return "B"
    elif perc<=60 and perc>50:
        return "C+"
    elif perc<=50 and perc>40:
        return "C"
    else:
        return "Fail"
print("Enter the Marks of five subjects: ")
sub1=int(input("Enter the marks of DSA= "))
sub2=int(input("Enter the marks of Python= "))
sub3=int(input("Enter the marks of Web_Development)= "))
sub4=int(input("Enter the marks of Simulation and Modeling= "))
sub5=int(input("Enter the marks of DBMS= "))
tm=total_marks(sub1,sub2,sub3,sub4,sub5)
pc= percentage(tm)
div=division(pc)
print(f"Total Marks= {tm}")
print(f"Percentage= {pc}")
print(f"Total Marks= {div}")
print("FAIL") if pc<40 else print("PASS")