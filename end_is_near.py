# The End Is Near But Not Here
# Write a function that returns the next to last word
# in the string argument.

# Words are any sequence of non-blank characters.

# You may assume that the input string will always
# contain at least two words.


def penultimate(words):
    word_list = words.split(" ")
    return word_list[-2]


# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")


# Further Exploration
# Our solution ignored two edge cases since we
# explicitly stated that you didn't have to handle
# them: strings that contain no words or just one
# word.

# Suppose we need a function that retrieves the
# middle word of a phrase/sentence. What edge cases
# need to be considered? How would you handle those
# edge cases without ignoring them? Write a function
# that returns the middle word of a phrase or
# sentence. It should handle all of the edge cases
# you thought of.
