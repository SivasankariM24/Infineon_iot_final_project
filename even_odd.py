# Function to check if a number is even
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Taking input from the user
num = int(input("Enter a number: "))

# Checking and displaying the result
if is_even(num):
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")
