# Tempeature Converter

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

if __name__ == "__main__":
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    ch = input("Choose 1 or 2: ")
    if ch == "1":
        c = float(input("Enter temperature(Celsius): "))
        f = celsius_to_fahrenheit(c)
        print(f"{c:.2f}C = {f:.2f}F")
    
    elif ch == "2":
        f = float(input("Enter temperature(Fahrenheit): "))
        c = fahrenheit_to_celsius(f)
        print(f"{f:.2f}F == {c:.2f}C")
    
    else:
        print("Invalid Choice. Select 1 or 2.")