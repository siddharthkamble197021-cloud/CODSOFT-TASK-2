num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))

print("1-addition")
print("2-subtraction")
print("3-multiplication")
print("4-division")

choice =int(input("enter your choice from 1-4:")) 

if choice == 1:
    print(num1+num2)
elif choice == 2:
    print(num1-num2)
elif choice == 3:
    print(num1*num2)
elif choice ==4:
    print(num1/num2)
else:
    print("invalid input")
