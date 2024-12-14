# Kyler Santos

#11/25/2024

#P2HW2

#A program to input grades and get information back on them using lists.

#Necessary inputs in float to allow decimals
mod1_grade = float(input('Enter grade for Module 1: '))
mod2_grade = float(input('Enter grade for Module 2: '))
mod3_grade = float(input('Enter grade for Module 3: '))
mod4_grade = float(input('Enter grade for Module 4: '))
mod5_grade = float(input('Enter grade for Module 5: '))
mod6_grade = float(input('Enter grade for Module 6: '))

#List to store grades from input
grades_list = [mod1_grade, mod2_grade, mod3_grade, mod4_grade, mod5_grade, mod6_grade]

#Calculate average and store as a variable
avg_grades_list = sum(grades_list) / len(grades_list)

print('\n')

#Display results using f string to allow alignment
print('----------Results----------')

print(f'{'Lowest Grade:':20} {min(grades_list)}')
print(f'{'Highest Grade:':20} {max(grades_list)}')
print(f'{'Sum of Grades:':20} {sum(grades_list)}')
print(f'{'Average:':20} {avg_grades_list:.2f}')

print('----------------------------------')

