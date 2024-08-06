anton_age = 21
beth_age = anton_age + 6
chen_age = beth_age + 20
drew_age = chen_age + anton_age
ethan_age = chen_age
print(f"Anton is {anton_age} years old.")
print(f"Beth is {beth_age} years old.")
print(f"Chen is {chen_age} years old.")
print(f"Drew is {drew_age} years old.")
print(f"Ethan is {ethan_age} years old.")

name = "Alice"
age = 30
city = "New York"
sentence = f"{name} is {age} years old and lives in {city}."
print(sentence)


s = "hElLo WoRlD"
capitalized = s.capitalize()
uppercase = s.upper()
lowercase = s.lower()
print(f"Original string: {s}")
print(f"Capitalized: {capitalized}")
print(f"Uppercase: {uppercase}")
print(f"Lowercase: {lowercase}")

s1 = "the quick brown fox jumps over the lazy dog"
index_of_fox = s1.find("fox")
count_of_the = s1.count("the")
print(f"The index of 'fox' is {index_of_fox}")
print(f"The number of occurrences of 'the' is {count_of_the}")


s2 = "I love programming in Python"
new_s = s2.replace("Python", "Java")
print(new_s)


s3 = "apple,banana,cherry,dates"
substrings = s3.split(',')
joined_string = ' '.join(substrings)
print(f"List of substrings: {substrings}")
print(f"Joined string: {joined_string}")


s4 = "   Python is fun!   "
trimmed_s4 = s4.strip()
left_justified = trimmed_s4.ljust(20, '*')
right_justified = trimmed_s4.rjust(20, '*')
print(f"Original string: '{s4}'")
print(f"Trimmed string: '{trimmed_s4}'")
print(f"Left justified: '{left_justified}'")
print(f"Right justified: '{right_justified}'")


num = 45
binary_representation = bin(num)
print(f"The binary representation of {num} is {binary_representation}")


base = 3
exponent = 4
result = base ** exponent
print(f"{base} raised to the power of {exponent} is {result}")


value = 12.34567
nearest_integer = round(value)
two_decimal_places = round(value, 2)
print(f"Original value: {value}")
print(f"Rounded to the nearest integer: {nearest_integer}")
print(f"Rounded to two decimal places: {two_decimal_places}")
