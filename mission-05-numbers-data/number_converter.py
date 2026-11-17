# Number Converter
# This program takes a decimal number from the user
# and converts it to binary and hexadecimal

number = int(input("Enter a positive decimal number: "))

binary_result = bin(number)
hex_result = hex(number)

print(f"Decimal: {number}")
print(f"Binary:  {binary_result}")
print(f"Hexadecimal: {hex_result}")
