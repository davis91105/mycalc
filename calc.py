# calculator.py
def hex_add(a, b):
    return hex(int(a, 16) + int(b, 16))

def hex_subtract(a, b):
    return hex(int(a, 16) - int(b, 16))

if __name__ == "__main__":
    print("Hexadecimal Calculator")
    x = input("Enter first hex number (e.g., 0x1A): ")
    y = input("Enter second hex number (e.g., 0x0F): ")
    print("Hex Sum:", hex_add(x, y))
    print("Hex Difference:", hex_subtract(x, y))
