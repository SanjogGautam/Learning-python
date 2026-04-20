try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = num1 / num2

except ZeroDivisionError:
    print("Oops! You cannot divide by zero.")

# except ValueError:
#print("Invalid input! Please enter numb12ers only.")

except Exception as e:
    # This catches ANY other error we didn't specify
    print(f"Something went wrong: {e}")

else:
      print(f"Result: {result}")

finally:#this runs no matter what
    print("Execution complete. (I always run!)")