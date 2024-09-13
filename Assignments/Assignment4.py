def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Step 1: Gather user information
def main():
    
    name = input("Enter your name: ")
    
# Step 2: Gather three favorite numbers
    numbers = []
    for i in range(3):
        number = int(input(f"Enter your {['first', 'second', 'third'][i]} favorite number: "))
        numbers.append(number)
    
# Step 3: Greet the user
    print(f"\nHello, {name}! Let's explore your favorite numbers:")
    
# Step 4: Determine if the numbers are even or odd
    even_odd_info = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]
    
# Step 5: Display even/odd information
    for num, info in even_odd_info:
        print(f"The number {num} is {info}.")
    
# Step 6: Calculate the square of each number and print the results
    print("\nNow, let's look at the squares of your numbers:")
    for num in numbers:
        print(f"The number {num} and its square: ({num}, {num ** 2})")
    
# Step 7: Calculate and print the sum of the numbers
    total_sum = sum(numbers)
    print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")
    
# Step 8: Check if the sum is a prime number
    if is_prime(total_sum):
        print(f"Wow, {total_sum} is a prime number!")
    else:
        print(f"{total_sum} is not a prime number, but it's still a great sum!")
    
if __name__ == "__main__":
    main()
