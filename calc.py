# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    print("Decimal Calculator")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print("Sum:", add(x, y))
    print("Difference:", subtract(x, y))
