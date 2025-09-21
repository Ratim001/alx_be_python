
# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# While loop to go through rows
while row < size:
    # For loop to print stars in each row
    for col in range(size):
        print("*", end="")  # stay on same line
    print()  # move to next line after finishing a row
    row += 1