# -*- coding: utf-8 -*-

import sys

#levels---------------	-----------------	-----------------	----------------

easy_level = """
EASY:

My ____1____ is ____2____ ____3____ with ____4____ if you want to ____5____.

Possible words = Terminator, John Connor, name, live, come, me.
"""

easy_level_answers = ["Terminator","name","John Connor","come","me","live"]

medium_level = """
MEDIUM:
			 Sometimes it is the ____1____ no one imagines
			 anything of who do the ____2____ no one can ____3____.
			 --____4____--

Possible words = Alan Turing, people, things, imagine, Nelson Mandela
			   """

medium_level_answers = ["Nelson Mandela","people","things","imagine","Alan Turing"]

hard_level = """
HARD:
			The ____1____ function is used to create lists containing arithmetic progressions. It is most often used in for loops.
			This is a method not an operand that helps you find strings in strings, this method is ____2____.
			The ____3____ allows to modify a list after we created it.
			The Action of ____4____ helps you to identify the causes that produces errors in the code.
			____5____ refers when you break a big problem into smaller problems, it makes easier to understand the big picture.

Possible words = find, System Thinking, Aliasing, Mutation, range, Debbuging

            """

hard_level_answers = ["Aliasing","range","find","Mutation","Debbuging","System Thinking"]

levels = ["easy","medium","hard"]

easy = ["Easy", "easy", "EASY"]
medium = ["Medium", "medium", "MEDIUM"]
hard = ["Hard", "hard", "HARD"]

#levels---------------	-----------------	-----------------	----------------

#Level selection---------------	-----------------	-----------------	----------------

def select_level (prompt):
#This function contains the levels and answers
#for each level, the function questions will use this
#function to locate answers and levels.
	if prompt in easy:
		level = easy_level
		level_answers = easy_level_answers
	elif prompt in medium:
		level = medium_level
		level_answers = medium_level_answers
	elif prompt in hard:
		level = hard_level
		level_answers = hard_level_answers
	return questions (level, level_answers)


#Level selection---------------	-----------------	-----------------	----------------

def opportunities(answer, level_answers, blank):
    '''This function prompts the user when they put an incorrect answer
    It analize all the answers in the levels and moves to the next
    question when answer is correct, to do that it goes through the
    def questions function'''
    while answer != level_answers[blank]:
        print "Incorrect answer try again..."
        answer = raw_input("Question:"+str(blank)+"?: ")
        if answer == level_answers[blank]:
            return answer  

def questions(level, level_answers):
    '''This function goes through all the questions
    and replace the spaces with answers. Once a question is
    answered, it skip to the next question.'''
    loc_number = ''
    blank = 1
    while loc_number != -1:
        print level
        answer = raw_input("What's the answer to number "+str(blank)+"?: ")
        if answer != level_answers[blank]:
            opportunities(answer, level_answers, blank)
        loc_number = level.find("____"+str(blank)+"____")
        location = level[loc_number:loc_number+9]
        level = level.replace(location,level_answers[blank])
        blank +=  1
        loc_number = level.find("____"+str(blank)+"____")
    print level + """
    Level Completed :) Congrtulations !!!
    """

def mad_libs_level():
    '''This fuction welcomes the user and prompt them asking the level desired. It goes 
    through the select_level function and links the level.'''
    prompt = raw_input("Welcome to Eduardo's Mad Libs, please select a level: easy, medium, hard: ")
    while prompt not in levels:
        print "Choose between easy, medium or hard."
        prompt = raw_input("Welcome to Eduardo's Mad Libs, please select a level: easy, medium, hard: ")
        if prompt in levels:
            continue
    return select_level(prompt)


mad_libs_level()







