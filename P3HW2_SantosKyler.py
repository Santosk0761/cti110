# Kyler Santos

# 11/26/2024

# P3HW2

# A program to determine and neatly display a workers pay

#Input
name = input("Enter employee's name: ")
hours_worked = float(input('Enter number of hours worked: '))
pay_rate = float(input("Enter employee's pay rate: "))

#Calculations using if than statements where necessary
if hours_worked > 40:
    overtime_hours = hours_worked - 40
else:
    overtime_hours = 0
if overtime_hours > 0:
    overtime_pay = (pay_rate * 1.5) * overtime_hours
else:
    overtime_pay = 0

reghour_pay = (hours_worked - overtime_hours) * pay_rate
gross_pay = reghour_pay + overtime_pay


#Output using f string to neatly line things up
print('--------------------------------------')
print(f'{'Employee name:':16} {name}')
print()
print(f'{'Hours Worked':<14} {'Pay Rate':<14} {'OverTime':<14} {'OverTime Pay':<16} {'RegHour Pay':<16} {'Gross Pay':<16}')
print('--------------------------------------------------------------------------------------------------')
print(f'{hours_worked:<14.1f} {pay_rate:<14.1f} {overtime_hours:<14.1f} ${overtime_pay:<16.2f} ${reghour_pay:<16.2f} ${gross_pay:<16.2f}')


