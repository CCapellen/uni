"""
This script displays a quiz in the format "Q:" and "A:" in alternating lines.
They are followed by the question and the answer. Each can only be one line
"""
from __future__ import print_function
import random

# To add: multiple file support
# picture support
# multiple line answers 


# raw_input is input in python 3
try:
    input = raw_input
except NameError:
    pass

try:
    open = file
except NameError:
    pass

def quiz():
    filename = str(input('Please enter the filename without spaces or " :'))
    f = open(filename, "r")
    questions = []
    answers = []

    for line_number,line in enumerate(f,1):
        if line[0]=='Q' or line[0] == 'q':
            questions.append(line)
        elif line[0]=='A' or line[0] == 'a':
            answers.append(line)
        else:
            print('Line %s does not start with a "Q" or "A".' % line_number)
    if len(questions) != len(answers):
        raise Exception('There are not the same number of questions as answers.')

    studyplan = list(range(len(questions)))

    response = str(input("\nShould the questions be in random order?"))
    if response[0] == "Y" or response[0]=="y":
        random.shuffle(studyplan)
    newstudyplan = []

    print("\nWelcome to the quiz. Press q or Q to quit while in the quiz. N or n to answer no, if you didn't get the question right and it will be asked again later. \n\n")

    while(len(studyplan)>0):
        for q in studyplan:
            print(questions[q])
            response = input("Do you want to see the answer?")
            if len(response)>0:
                if response[0]=='Q' or response[0]=='q':
                    studyplan = []
                    newstudyplan = []
                    break
            print("\n" + str(answers[q]))
            response = input("did you get it right?: ")
        if len(response)>0:
            if response[0]=="N" or response[0] == 'n':
                newstudyplan.append(q)
            print("\n\n")
        if len(newstudyplan)>1:
            studyplan = random.shuffle(newstudyplan)
            newstudyplan = []
        else:
            studyplan = newstudyplan
            newstudyplan = []

    print("You are done!!!")

quiz()
