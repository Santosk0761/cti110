#Kyler Santos

#11/2/2024

#P5HW

#A program to simulate a simple math quiz

#Necessary to use the random number function
import random

#Function to generate random numbers and put them in alist so they can be called
def random_numbers():
    return random.randint(1, 100), random.randint(1, 100)

#Function to add numbers
def add_numbers(number1, number2):
    print(f'{number1}')
    print(f'+{number2}')
    print()
    return number1 + number2

#Function to subtract numbers
def subtract_numbers(number1, number2):
    print(f'{number1}')
    print(f'-{number2}')
    print()
    return number1 - number2

print('Welcome to Math Quiz')
print('\n')

option = 0

#So that the program loops as long as option 3 is not selected
while option != '3':

    number1, number2 = random_numbers()
    num_guess = 0

    print('MAIN MENU')
    print('---------------')
    print('1. Adding Random Numbers')
    print('2. Subtracting Random Numbers')
    print('3. Exit')
    print()

    option = input('Please choose one of the menu options: ')

    #If statements that correspond to our selected option and calls necessary function
    if option == '1':
        solution = add_numbers(number1, number2)

    elif option == '2':
        solution = subtract_numbers(number1, number2)
        
    elif option == '3':
        print('Thank you for playing...')
        print('Bye!!')
        break
    else:
        print('Invalid option. Please Try again.')
        continue

    answer = int(input('Enter answer. \n'))

   #Program loops until given a correct answer
    while answer != solution:
        num_guess += 1
        
        if answer < solution:
            print('Sorry, guess is too low')
            print()
        elif answer > solution:
            print('Sorry, guess is too high')
            print()

        answer = int(input('Try again: '))

    #Once given a correct answer and the nested loop ends going back to the start
    num_guess += 1
    print('Congratulations!!!! Your answer is correct.')
    print(f'Number of guesses: {num_guess}')
    print()

    
          
        
    
        

    

    

