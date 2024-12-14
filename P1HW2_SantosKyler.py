#Kyler Santos
#11/23/2024
#P1HW2
#A program to calculate and display travel expenses

print('This program calculates and displays travel expenses')

#Input estimated budget and expenses
budget = int(input('Enter budget: '))
print('\n')
travel_dest = input('Enter travel destination: ')
print('\n')
gas = int(input('How much will you spend on gas?: '))
print('\n')
accoma = int(input('How much will you spend on accomadation?: '))
print('\n')
food = int(input('How much will you spend on food?: '))

#Calculations for total_expenses and rem_balance
total_expenses = gas+accoma+food
rem_balance = budget-total_expenses

print('\n')

#Display output
print('-------Travel Expenses-------')
print('Location: ', travel_dest)
print('Initial Budget: ', budget)

print('\n')

print('Fuel: ', gas)
print('Accomadation: ',accoma)
print('Food: ', food)

print('\n')

print('Remaining Balance: ', rem_balance)

