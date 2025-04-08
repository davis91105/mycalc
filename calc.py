# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def hex_add(a, b):
    return hex(int(a, 16) + int(b, 16))

def hex_subtract(a, b):
    return hex(int(a, 16) - int(b, 16))

if __name__ == "__main__":
    mode = input("Choose mode (decimal/hex): ").strip().lower()

    if mode == "decimal":
        print("Decimal Calculator")
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print("Sum:", add(x, y))
        print("Difference:", subtract(x, y))
    elif mode == "hex":
        print("Hexadecimal Calculator")
        x = input("Enter first hex number (e.g., 0x1A): ")
        y = input("Enter second hex number (e.g., 0x0F): ")
        print("Hex Sum:", hex_add(x, y))
        print("Hex Difference:", hex_subtract(x, y))
    else:
        print("Invalid mode.")
