
"""This program will create a user-operated mad-libs! Enjoy!."""


print "Mad Libs has started"
name = raw_input("Enter your name: ")

print 'Three adjectives please!'
adjective_a = raw_input("First adjective: ")
adjective_b = raw_input("Second adjective: ")
adjective_c = raw_input("Third adjective: ")

print 'Three verbs please!'
verb_a = raw_input("First verb: ")
verb_b = raw_input("Second verb: ")
verb_c = raw_input("Third verb: ")

print 'Four nouns please!'
noun_a = raw_input("First noun: ")
noun_b = raw_input("Second noun: ")
noun_c = raw_input("Third noun: ")
noun_d = raw_input("Fourth noun: ")

print 'Enter the following please!'

animal = raw_input("Enter an animal: ")
food = raw_input("Enter a food: ")
fruit = raw_input("Enter a fruit: ")
number = raw_input("Enter a number: ")
superhero_name = raw_input("Enter a superhero name: ")
country = raw_input("Enter a country: ")
dessert = raw_input("Enter a dessert: ")
year = raw_input("Enter a year: ")

#The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rhythm of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world."

print STORY % (adjective_a, name, verb_a, adjective_b, noun_a, noun_b, animal, food, verb_b, noun_c, fruit, adjective_c, name, verb_c, number, name, superhero_name, superhero_name, name, country, name, dessert, name, year, noun_d)
