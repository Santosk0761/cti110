# Kyler Santos
# 11/25/2024
# P2LAB2
# A program to use dictionary

cars = {
    'Camaro': 18.21,
    'Prius': 52.36,
    'Model S': 110,
    'Silverado': 26,
}

keys = cars.keys()

#Display the created dictionary
print(keys)
print('\n')

#Input car choice and use that input to pull up the corresponding value in dictionary
car_choice = input("Enter a vehicle to see it's mpg: ")
print('\n')

mpg = cars[car_choice]

print(f'The {car_choice} gets {mpg} mpg.')
print('\n')

#Input miles driven and use that to calculate efficiency
miles_driven = float(input(f'How many miles will you drive the {car_choice}?: '))
print('\n')

car_eff = miles_driven / mpg

print(f'{car_eff:.2f} gallon(s) of gas are needed to drive the {car_choice} {miles_driven} miles.')

      


