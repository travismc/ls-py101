# Madlibs
# Madlibs is a simple game where you create a story template 
# with "blanks" for words. You, or another player, then 
# construct a list of words and place them into the story, 
# creating an often silly or funny story as a result.

# Create a simple madlib program that prompts for a noun, 
# a verb, an adverb, and an adjective, and injects them 
# into a story that you create.


noun = input("Type a noun: ")
verb = input("Type a verb: ")
adjective = input("Type an adjective: ")
adverb = input("Type an adverb: ")

print(f"Why is you {adjective} {noun} trying to {verb} {adverb} without you?")



# Example
# Enter a noun: dog
# Enter a verb: walk
# Enter an adjective: blue
# Enter an adverb: quickly
# Expected OutputCopy Code
# Do you walk your blue dog quickly? That's hilarious!
# The blue dog walks quickly over the lazy dog.
# The dog quickly walks up to Joe's blue turtle.