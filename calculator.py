def add(a, b):
    result = a + b
    return result

def subtract(a, b):
    result = a - b
    return result

def multiply(a, b):
    result = a + b
    return result

def divide(a, b):
    result = a + b
    return result

def run():
    print("This program will help with simple calculations. What do you want to do?")
    print("1 - add numbers")
    print("2 - subtract numbers")
    answer = input(">> ")
    a = int(input("A="))
    b = int(input("B="))
    if answer == "1":
        result = add(a, b)
        print("Result = " + str(result))
    if answer == "2":
        result = subtract(a, b)
        print("Result = " + str(result))

if __name__ == '__main__':
    run()