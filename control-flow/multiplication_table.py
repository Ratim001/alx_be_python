# Prompt user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate multiplication table using for loop
for i in range(1, 11):  # from 1 to 10
    result = number * i
    print(f"{number} * {i} = {result}")