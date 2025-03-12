print("Welcome to the Calculator.py")
print("Please Chose your operations :")
print("1. Addition ")
print("2. Subtraction")
print("3. Multiplication ")
print("4. Division ")
print("5. Square ")
print("6. Cube ")
print("7. Exit ")
choice=int(input("Enter your choice (1-7) :"))

if choice == 1:
     print("Great choice")
     #Addition
     num1 = float(input("Number 1 = "))
     num2 = float(input("Number 2 = "))
     result=num1+num2
     print("The result is = ",result)
elif choice == 2:
     print("I think you need help in calculating in your Maths homework am i right??")
     print("Well it is good . Now i will help you , then you show the homework to your maths teacher!!!!")
     #Subtraction
     num1 = float(input("Number 1 = "))
     num2 = float(input("Number 2 = "))
     result=num1-num2
     print("The result is = ",result)
elif choice == 3:
    print("Nice choice ")
    print("I know that this operation is hard,so i'll help you")
    #Multiplication
    num1 = float(input("Number 1 = "))
    num2 = float(input("Number 2 = "))
    result=num1*num2
    print("The result is = ",result)
elif choice == 4:
    print("Wow , Amazing Choice ")
    #Division
    num1 = float(input("Number 1 = "))
    num2 = float(input("Number 2 = "))
    result=num1/num2
    print("The result is = ",result)
elif choice == 5:
    print("Nice!You are Trying to learn squares . I will help you with that")
    #Square 
    num1 = float(input("Number 1 = "))
    result=num1**2
    print("The result is = ",result)
elif choice == 6:
    print("Nice!You are Trying to learn Cubes . I will help you with that")
    #Cube
    num1 = float(input("Number 1 = "))
    result=num1**3
    print("The result is = ",result)
elif choice ==7:
    print("Thank you my friend for using the Calculator ")
    print("Visit again")
else:
    print("Invalid choice. Pls choose Between (1-7) So that i can help you")


