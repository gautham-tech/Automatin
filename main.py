print("average calculator")
print("percentage calculator")
print("Press 1: Average Calculator")
print("Press 2: Percentage Calculator")
number=int(input("Choose a number: 1 or 2 ? "))
if (number == 1):
    maths=int(input("Enter your Maths marks:"))
    science=int(input("Enter your Science marks:"))
    english=int(input("Enter your English marks:"))
    average=(maths+science+english)/3
    print("Your average marks are:",average)

elif (number == 2):
    maths=int(input("Enter your Maths marks:"))
    science=int(input("Enter your Science marks:"))
    english=int(input("Enter your English marks:"))
    sum=maths+science+english
    total=300
    percentage=(sum/300)*100
    print("Your total Percentage is:",percentage)

else:
    print("Sorry choose a valid option")