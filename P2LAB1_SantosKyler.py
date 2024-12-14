# Kyler Santos
# 11/24/2024
# P2LAB1
# A program to calculate and output the diameter, circumference, and area of a circle given the radius

#Input
radius = float(input('Enter the radius of the circle: '))
print('\n')

#I think this is necessary to use math.pi
import math

#Calculations
diameter = 2 * radius
circum = 2 * math.pi * radius
area = math.pi * (radius ** 2)

#The output of the calculations
print('The diameter of the circle is: ', f'{diameter:.1f}')
print('\n')
print('The circumference of the circle is: ', f'{circum:.2f}')
print('\n')
print('The area of the cicle is: ', f'{area:.3f}')




      
