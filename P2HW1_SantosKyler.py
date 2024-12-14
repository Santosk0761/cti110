#Kyler Santos
#11/25/2024
#P2HW1
#A program to calculate and display travel expenses

print('This program calculates and displays travel expenses')

#Input estimated budget and expenses
budget = float(input('Enter budget: '))
print('\n')

travel_dest = input('Enter travel destination: ')
print('\n')
gas = float(input('How much will you spend on gas?: '))
print('\n')
accoma = float(input('How much will you spend on accomadation?: '))
print('\n')
food = float(input('How much will you spend on food?: '))

#Calculations for total_expenses and rem_balance
total_expenses = gas+accoma+food
rem_balance = budget-total_expenses

print('\n')

#Display output
print('----------Travel Expenses----------')

print(f'{'Location:':20} {travel_dest}')
print(f'{'Initial Budget:':20} ${budget:.2f}')
print(f'{'Fuel:':20} ${gas:.2f}')
print(f'{'Accomadation:':20} ${accoma:.2f}')
print(f'{'Food:':20} ${food:.2f}')

print('-----------------------------------')

print('\n')

print(f'{'Remaining Balance:':20} ${rem_balance:.2f}')
