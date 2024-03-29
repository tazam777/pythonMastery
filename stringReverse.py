
def stringRV(s):
    string_empty = ""
    for char in s:
        string_empty = char + string_empty
    return string_empty
    

def getString():
    return input("Enter string to be reversed: ")

if __name__ == "__main__":
    reversed_string = stringRV(getString())
    print("Reversed:", reversed_string)


