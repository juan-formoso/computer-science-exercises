# Write a pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours. Use try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program.

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    float_hours = float(hours)
    float_rate = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

print(float_hours, float_rate)

if float_hours > 40:
    pay = 40 * float_rate + (float_hours - 40) * float_rate * 1.5
else:
    pay = float_hours * float_rate

print('Pay:', pay)
