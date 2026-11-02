# Multiple exception handling example

try:
    num = int(input("Enter your age please: "))
    result = 100 / num

    my_list = [10, 20, 30]
    print("Selected value:", my_list[num])

except ValueError:
    print("Error: Please enter numbers only.")

except ZeroDivisionError:
    print("Error: Age cannot be zero because division by zero is not allowed.")

except IndexError:
    print("Error: Your number is outside the list range.")

except Exception as e:
    print("Unexpected error:", e)

finally:
    print("Program finished successfully.")