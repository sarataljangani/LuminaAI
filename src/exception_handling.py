try:
    number = int(input("Enter a number: "))

    result = 100 / number
    print("Result =", result)

except ZeroDivisionError:
    print("You cannot divide by zero.")

except ValueError:
    print("Please enter a valid integer.")