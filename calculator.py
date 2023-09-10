def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def modulo(a,b):
    return a%b

print("Please select the operation: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulo")

choice = input("Please enter your choice(1/ 2/ 3/ 4): ")

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

if choice == '1':
    print(num1 ,"+", num2,"=",add(num1,num2))

elif choice == '2':
    print(num1 ,"-", num2,"=",subtract(num1,num2))

elif choice == '3':
    print(num1 ,"*", num2,"=",multiply(num1,num2))

elif choice == '4':
    print(num1 ,"/", num2,"=",divide(num1,num2))

elif choice == '5':
    print(num1 ,"%", num2,"=",modulo(num1,num2))

else:
    print("This is a invalid input")
