#Kyler Santos
#12/1/2024
#P5LAB
#A program to simulate a customer using a self checkout machine using functions.

def main():

    import random
    
    def disperse_change(cash_in_machine):

        money = cash_in_machine - owed_money
        
        print(f'Change is: ${money:.2f}')
        print()

        total_cents = round(money * 100)
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

    owed_money = round(random.uniform(0.01, 100.00), 2) 

    print(f'You owe ${owed_money:.2f}')

    cash_in_machine = float(input('How much cash will you put in the machine? '))

    disperse_change(cash_in_machine)

main()

