# Decimal to Binary Converter

# Ask the user for a decimal number
decimal = int(input("Enter a decimal number: "))

# Convert to binary using the built-in bin() function
binary = bin(decimal)

# Remove the '0b' prefix and print the result
print("Binary value is:", binary[2:])
