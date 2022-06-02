# Write a pay computation with time-and-a-hald for overtime and create a function called computepay which takes two parameters (hours and rate).

def computepay(hours, rate):
    try:
        hours = float(hours)
        rate = float(rate)
    except:
        print('Error, please enter numeric input')
        quit()
    if hours > 40:
        overtime = hours - 40
        pay = 40 * rate + overtime * 1.5 * rate
    else:
        pay = hours * rate
    return pay

hours = input('Enter Hours: ')
rate = input('Enter Rate: ')

payment = computepay(hours, rate)

print('Pay:', payment)