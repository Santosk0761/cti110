# Kyler Santos

# 11/26/2024

# P3LAB

# A program to calculate coins to make up a given amount of money

#Input
money = float(input('Enter the amount of money as a float: $'))

#Calculations
total_cents = money * 100
total_cents = int(total_cents)

dollars = total_cents // 100
total_cents = total_cents - (dollars * 100)

quarters = total_cents // 25
total_cents = total_cents - (quarters * 25)

dimes = total_cents // 10
total_cents = total_cents - (dimes * 10)

nickels = total_cents // 5
total_cents = total_cents - (nickels * 5)

pennies = total_cents

#Output
if money <= 0:
    print('No Change')
if dollars > 0:
    if dollars < 2:
        print(dollars, 'Dollar')
    else:
        print(dollars, 'Dollars')
if quarters > 0:
    if quarters < 2:
        print(quarters, 'Quarter')
    else:
        print(quarters, 'Quarters')
if dimes > 0:
    if dimes < 2:
        print(dimes, 'Dime')
    else:
        print(dimes, 'Dimes')
if nickels > 0:
    if nickels < 2:
        print(nickels, 'Nickel')
    else:
        print(nickels, 'Nickels')
if pennies > 0:
    if pennies < 2:
        print(pennies, 'Penny')
    else:
        print(pennies, 'Pennies')




