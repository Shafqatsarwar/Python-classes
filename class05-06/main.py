# def className():
#     print("Learning Python")

#     def get_user_name(age: str):
#         my_name: str = input("Enter your name: ")
#         age = input("Enter your age!")
#         print("Hello", my_name)
#         return my_name
#     new_user_name: str = get_user_name()
#     print(f"Hello, {new_user_name}")
# className()

def add_two_numbers(num1, num2):
    return num1 + num2

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    result = add_two_numbers(num1, num2)
    
    print(f"The sum of {num1} and {num2} is {result}")

if __name__ == "__main__":
    main()


def main():
    favorite_animal = input("What is your favorite animal? ")
    print(f"My favorite animal is also {favorite_animal}!")

if __name__ == "__main__":
    main()


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def main():
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    
    celsius = fahrenheit_to_celsius(fahrenheit)
    
    print(f"The temperature in Celsius is {celsius:.2f}")

if __name__ == "__main__":
    main()


# Function to calculate the perimeter of a triangle
def calculate_perimeter(side1, side2, side3):
    return side1 + side2 + side3

def main():
    side1 = float(input("Enter the length of the first side: "))
    side2 = float(input("Enter the length of the second side: "))
    side3 = float(input("Enter the length of the third side: "))
    
    perimeter = calculate_perimeter(side1, side2, side3)
    
    print(f"The perimeter of the triangle is {perimeter}")

if __name__ == "__main__":
    main()


# Function to calculate the square of a number
def calculate_square(number):
    return number * number

def main():
    number = float(input("Enter a number: "))
    
    square = calculate_square(number)
    
    print(f"The square of {number} is {square}")

if __name__ == "__main__":
    main()

numbers = [1, 2, 3, 4, 5]

numbers.remove(3)

print(numbers)


# List of items
items = [10, 20, 30, 40]

removed_item = items.pop()

print(f"Updated list: {items}")
print(f"Removed item: {removed_item}")

colors = ['red', 'blue', 'green', 'yellow']

index_of_green = colors.index('green')

print(f"The index of 'green' is {index_of_green}")


def get_last_element(lst):
    print(lst[-1])

example_list = [1, 2, 3, 4, 5]
get_last_element(example_list)  # This will print: 5


def main():
    values = []
    
    while True:
        value = input("Enter a value (or press Enter to finish): ")
        
        if value == "":
            break
        
        values.append(value)
    
    print("The list of values is:", values)

if __name__ == "__main__":
    main()

# Main function
def main():
    values = []
    
    while True:
        value = input("Enter a value: ")
        
        if value == "":
            break
        
        values.append(value)
    
    print("Here's the list:", values)

if __name__ == "__main__":
    main()
