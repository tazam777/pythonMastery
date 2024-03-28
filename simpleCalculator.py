def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cannot Divide by Zero"
    else:
        return a / b

def prompt():
    print("Enter the operation to perform:")
    print("1 for Addition")
    print("2 for Subtraction")
    print("3 for Multiplication")
    print("4 for Division")
    print("5 to Exit")

def get_numbers():
    a=float(input("Enter Number 1"))
    b=float(input("Enter Number 2"))
    return a,b
    


def core_logic():
    while True:
        prompt()
        choice = input("Choice: ")
        if choice in ['1', '2', '3', '4']:
            a, b = get_numbers()
            if choice == '1':
                result = add(a, b)
            elif choice == '2':
                result = sub(a, b)
            elif choice == '3':
                result = mul(a, b)
            elif choice == '4':
                result = div(a, b)
            print("Result:", result)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 5.")

if __name__ == "__main__":
    core_logic()



