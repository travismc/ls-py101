# ddaaiillyy ddoouubbllee
# Write a function that takes a string argument 
# and returns a new string that contains the 
# value of the original string with all 
# consecutive duplicate characters collapsed 
# into a single character.

def crunch(string: str) -> str:
	crunched_string = []
	idx = 0
	
	while idx < len(string):
		if idx == len(string) - 1 or string[idx] != string[idx + 1]:
			crunched_string.append(string[idx])
		
		idx += 1

	return ''.join(crunched_string)

# Examples
# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')

print(crunch('ddaaiillyy ddoouubbllee'))
print(crunch('4444abcabccba'))
print(crunch('ggggggggggggggg'))
print(crunch('abc'))
print(crunch('a'))
print(crunch(''))


# Further Exploration
# Regular expressions are also available in 
# Python through the re module. If you're 
# familiar with regular expressions, you can 
# try to solve this problem using that module. 
# Additionally, can you think of any other 
# solutions that don't involve regular 
# expressions, perhaps using Python's built-in 
# string or list methods?
