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


def read_in_wordlist():
    filename = str(input('Please enter the filename without spaces or " :'))
    f = open(filename, "r")
    g = open(filename + "quiz", "w")
    line_number = 0
    for line in f:
        if len(line)>1: # ignore empty lines
            if line_number % 2 == 0:
                #questions.append(line)
                g.write("Q:  " + line)
            else:
                g.write("A:  " + line)
            line_number += 1 
    g.flush()
    g.close()
    f.close()

def save_dict(categories):
    for cat in categories.keys():
        g = open(cat, "w") 
        for q,a in categories[cat]:
            g.write(q)
            g.write(a)
        g.flush()
        g.close()
            
def sort_word_list():
    categories = {}
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
    
    print("\nWelcome to the quiz. Press q or Q to quit while in the quiz. N or n to answer no, if you didn't get the question right and it will be asked again later. \n\n")
    
    studyplan = list(range(len(questions)))
    
    response = str(input("\nShould the questions be in random order?"))
    if len(response)>0:
        if response[0] == "Y" or response[0]=="y":
            random.shuffle(studyplan)

    for q in studyplan:
        print('\n\n'+ questions[q])
        response = input("Do you want to see the answer?")
        if len(response)>0:
            if response[0]=='Q' or response[0]=='q':
                studyplan = [] # then while loop stops
                break
        print(str(answers[q]))
        response = input("which category should this word be?: ")
        print(categories.keys())
        if len(response)>0:
            if categories.get(response):
                categories[response].append([questions[q],answers[q]])
            else:
                categories[response] = [[questions[q],answers[q]]]
            if response[0]=='Q' or response[0]=='q':
                studyplan = [] # then while loop stops
                break

    print("You are done!!!")
    return categories
            
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
    
    print("\nWelcome to the quiz. Press q or Q to quit while in the quiz. N or n to answer no, if you didn't get the question right and it will be asked again later. \n\n")
    
    studyplan = list(range(len(questions)))
    newstudyplan = []
    
    
    response = str(input("\nShould the questions be in random order?"))
    if len(response)>0:
        if response[0] == "Y" or response[0]=="y":
            random.shuffle(studyplan)


    while(len(studyplan)>0):
        for q in studyplan:
            print('\n\n'+ questions[q])
            response = input("Do you want to see the answer?")
            if len(response)>0:
                if response[0]=='Q' or response[0]=='q':
                    studyplan = [] # then while loop stops
                    newstudyplan = []
                    break
            print(str(answers[q]))
            response = input("did you get it right?: ")
            if len(response)>0:
	            if response[0]=="N" or response[0] == 'n':
	                newstudyplan.append(q)
	            elif response[0]=='Q' or response[0]=='q':
                     studyplan = [] # then while loop stops
                     newstudyplan = []
                     break
        if len(newstudyplan)>=1:
            random.shuffle(newstudyplan)
            studyplan = newstudyplan
            newstudyplan = []
        else:
            studyplan = []
            newstudyplan = []

    print("You are done!!!")

quiz()
