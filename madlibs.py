"""
This program generates passages that are generated in mad-lib format
Author: Katherin
"""

# The template for the story

STORY = "This morning _ woke up feeling _. 'It is going to be a _ day!' Outside, a bunch of _s were protesting to keep _ in stores. They began to _ to the rhythm of the _, which made all the _s very _. Concerned, _ texted _, who flew _ to _ and dropped _ in a puddle of frozen _. _ woke up in the year _, in a world where _s ruled the world."

print 'Mad Libs has started.'

name = raw_input("Enter a name: ")

print 'You need to input 3 adjectives, one verb and two nouns!'

adjective1 = raw_input("Enter first adjective: ")
adjective2 = raw_input("Enter second adjective: ")
adjective3 = raw_input("Enter third adjective: ")

print 'Now one verb!'

verb =  raw_input("Enter Verb: ")

print 'Now two nouns!'

noun1 = raw_input("Enter first noun: ")
noun1 = raw_input("Enter second noun: ")
