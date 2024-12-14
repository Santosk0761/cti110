# Kyler Santos

# 11/26/2024

# P4HW2

# A program to determine and neatly display a workers pay. Also has the ability to take multiple workers input and display the total after displaying individual workers pay.

'''
Modify the program to handle and store the pay of multiple employees
Initialize necessary values
Set up the program to loop
Increase num_employees by 1 every loop
Make sure that the loop ends if user types "Done"
Print the total compiled pay of all employees info that has been entered
Modify program so that output is identical or close as possible to the given example
'''

#Initializing values
name = 'Go'
num_employees = 0
total_overtime_pay = 0
total_reg_pay = 0
total_gross_pay = 0

#Setting up program to loop unless the user has typed "Done"
while name != "Done":
    
    name = input('Enter employee\'s name or "Done" to terminate: ')

    #If statement that is only valid if the user does not enter "Done"
    if name != "Done":
    
        hours_worked = float(input(f'How many hours did {name} work? '))
        pay_rate = float(input(f"What is {name}'s pay rate? "))

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

        num_employees += 1
        total_overtime_pay += overtime_pay
        total_reg_pay += reghour_pay
        total_gross_pay += gross_pay


        #Output using f string to neatly line things up
        print()
        print(f'{'Employee name:':16} {name}')
        print()
        print(f'{'Hours Worked':<14} {'Pay Rate':<14} {'OverTime':<14} {'OverTime Pay':<16} {'RegHour Pay':<16} {'Gross Pay':<16}')
        print('--------------------------------------------------------------------------------------------------')
        print(f'{hours_worked:<14.1f} {pay_rate:<14.2f} {overtime_hours:<14.1f} ${overtime_pay:<16.2f} ${reghour_pay:<16.2f} ${gross_pay:<16.2f}')
        print('\n')

    #else break statement to restart the loop if given "Done" input, Done != Done is false thus completely ending the while loop and printing the necessary info
    else:
        break

#Prints after the loop is finished
print()
print(f'Total number of employees entered: {num_employees}')
print(f'Total amount paid for overtime: ${total_overtime_pay:.2f}')
print(f'Total amount paid for regular hours: ${total_reg_pay:.2f}')
print(f'Total amount paid in gross: ${total_gross_pay:.2f}')

