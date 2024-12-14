#Kyler Santos

#11/27/2024

#P4HW1

#A program to input grades and get information back on them using lists and for loops.

'''
Initialize grades_list and score_num
Ask user to enter number of scores they would like to enter.
Set up a for loop to collect those scores
If an invalid number is entered return "invalid score" and allow user to enter again without affecting the list
print the results using f string to allow things to evenly line up
Remove lowest score so that the modified list and average can be calculated
Use if statements to setup letter grade to show in results
'''


grades_list = []
score_num = 1

num_scores = int(input('How many scores do you want to enter? '))

for grade in range(num_scores):
    grade = float(input(f'Enter score #{score_num} : '))
    if grade >= 0 and grade <= 100:
        grades_list.append(grade)
        score_num +=1
    else:
        for grade in range(num_scores):
            print()
            print('INVALID Score entered!!!!')
            print('Score should be between 0 and 100')
            grade = float(input(f'Enter score #{score_num} again: '))
            if grade >= 0 and grade <= 100:
                grades_list.append(grade)
                score_num += 1
                break 

print('\n')
print('-------------Results-------------')
print(f'{'Lowest Score':14} : {min(grades_list):.1f}')

grades_list.remove(min(grades_list))

print(f'{'Modified List':14} : {grades_list}')

avg_grades_list = sum(grades_list) / len(grades_list)

print(f'{'Scores Average':14} : {avg_grades_list:.2f}')

if avg_grades_list >= 90:
    letter_grade = 'A'
elif avg_grades_list >= 80:
    letter_grade = 'B'
elif avg_grades_list >= 70:
    letter_grade = 'C'
elif avg_grades_list >= 60:
    letter_grade = 'D'
elif avg_grades_list < 60:
    letter_grade = 'F'

print(f'{'Grade':14} : {letter_grade}')

print('--------------------------------------')

