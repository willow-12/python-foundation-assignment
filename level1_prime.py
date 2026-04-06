# Program to check if a number is prime

num = int(input("Enter a number: "))

# Assume the number is prime
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

# Output result
if is_prime:
    print("It is a prime number.")
else:
    print("It is NOT a prime number.")
