#TODO: Write the functions for arithmatic operations here
#These functions should cover Task 2

def add(a, b):
    return a + b
    
def subtract(a, b):
    return a - b
    
def multiply(a, b):
    return a * b
    
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("float division by zero")
        return None
        
def power(a, b):
    return a ** b
    
def remainder(a, b):
    try:
        return a % b
    except ZeroDivisionError:
        print("float modulo by zero")
        return None

#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function sould cover Task 1 (Section 2) and Task 3

def select_op(choice):
    if choice == '#':
        return -1
        
    if choice == '$':
        return 0
        
    if choice not in ['+', '-', '*', '/', '^', '%']:
        print("Unrecognized operation")
        return 0
        
    # Get first number
    while True:
        num1_input = input("Enter first number: ")
        print(f"{num1_input}")
        
        # Check for terminate command
        if num1_input.endswith('#'):
            return -1
        # Check for reset command
        if num1_input.endswith('$'):
            return 0
            
        try:
            num1 = float(num1_input)
            break
        except ValueError:
            print("Not a valid number, please enter again")
            continue
        
    # Get second number
    while True:
        num2_input = input("Enter second number: ")
        print(f"{num2_input}")
        
        # Check for terminate command
        if num2_input.endswith('#'):
            return -1
        # Check for reset command
        if num2_input.endswith('$'):
            return 0
            
        try:
            num2 = float(num2_input)
            break
        except ValueError:
            print("Not a valid number, please enter again")
            continue
        
    # Perform calculation based on choice
    try:
        if choice == '+':
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif choice == '-':
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == '*':
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif choice == '/':
            result = divide(num1, num2)
            if result is not None:
                print(f"{num1} / {num2} = {result}")
            else:
                print(f"{num1} / {num2} = None")
        elif choice == '^':
            result = power(num1, num2)
            print(f"{num1} ^ {num2} = {result}")
        elif choice == '%':
            result = remainder(num1, num2)
            if result is not None:
                print(f"{num1} % {num2} = {result}")
    except Exception as e:
        print("Something Went Wrong")
        
    return 0

#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
    
    # take input from the user
    try:
        choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
        print(choice)
        result = select_op(choice)
        if result == -1:
            #program ends here
            print("Done. Terminating")
            exit()
    except EOFError:
        print("\nDone. Terminating")
        exit()