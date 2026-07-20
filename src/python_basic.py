# python_basics.py

# Program 1: Sum of two numbers
a = 10
b = 20
print("Program 1")
print("Sum =", a + b)
print()

# Program 2: Largest number among three numbers
x = 15
y = 8
z = 23

if x >= y and x >= z:
    largest = x
elif y >= x and y >= z:
    largest = y
else:
    largest = z

print("Program 2")
print("Largest =", largest)
print()

# Program 3: Multiplication table (1 to 10)
print("Program 3")

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} × {j} = {i*j}")
    print("-" * 20)

# Program 4: Sum of numbers from 1 to 100
total = 0

for i in range(1, 101):
    total += i

print("Program 4")
print("Sum =", total)
print()

# Program 5: Square function

def square(number):
    return number * number

print("Program 5")
print(square(6))




