binary = input("Enter a binary number: ")

try:
    decimal = int(binary, 2)
    print(f"The decimal value is: {decimal}")
except ValueError:
    print("Invalid binary number.")
