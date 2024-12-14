#Kyler Santos
#11/27/2024
#P4LAB2
#Use while loop and for loop together

run_again = 'yes'

while run_again != 'no':

    #User input
    user_num = int(input('Enter an integer: '))
    print() #Creating space between lines

    if user_num >= 0:
        #display multiplication for that value and range (1-12)
        for item in range(1, 13):
            print(f'{user_num} * {item} = {user_num * item}')
    else:
        print('This program does not handle negative numbers')
        
    print()
    #User input, if 'yes' the program will go again, if 'no' it will terminate
    run_again = input('Would you like to run the program again? ')
    print()

#loop has broken. User entered 'no'
print('Exiting program...')

