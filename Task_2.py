def sum(a, b):
    print(f"Sum of {a} and {b} is : {a+b}\n")
def diff(a, b):
    print(f"Difference of {a} and {b} is : {a-b}\n")
def multi(a, b):
    print(f"Multiplication of {a} and {b} is : {a*b}\n")
def div(a, b):
    print(f"Division of {a} and {b} is : {(a/b)}\n")
while True:
    print("~~~~~~~~~~~~~~~~~~Calculator~~~~~~~~~~~~~~~~~~\n")
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        op = input("Select Operator (+,-,*,/): ")

        if op == '+':
            sum(num1, num2)
        elif op == '-':
            diff(num1,num2)
        elif op == '*':
            multi(num1, num2)
        elif op == '/':
            div(num1,num2)
        else:
            print("Enter valid operator (+,-,*,/)\n")
    except:
        print("Enter valid Values!\n")
