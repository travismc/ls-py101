# When Will I Retire?
# Build a program that displays when the user will 
# retire and how many years she has to work till 
# retirement.

from datetime import date

year = date.today().year

age_now = int(input('What is your age? '))
age_retire = int(input('At what age would you like to retire? '))

years_to_go = age_retire - age_now
retire_year = year + years_to_go

print(f"It's {year}. You will retire in {retire_year}.")
	  
print(f"You have only {years_to_go} years of work to go!")
