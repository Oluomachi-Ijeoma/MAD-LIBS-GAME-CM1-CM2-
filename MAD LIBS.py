"""Creating a Mad Libs game for my CM1/CM2 students with little to no English background.
The goal of this game is to have fun while practicing topics we have learnt."""


daily_routine = input('Enter an activity in your daily routine, e.g go to bed, wake up, eat breakfast: ')
family = input('Enter a member of your family, e.g mum, dad: ')
place = input('Enter a place, e.g school, hospital: ')
colour = input ('Enter a colour, e.g white, black: ')
ordinal_number = input ('Enter a number, e.g first, second: ')
day = input ('Enter a day of the week, e.g monday: ')
month = input ('Enter a month of the year, e.g january, february: ')
time = input ('Enter a time of the day, e.g 8am, 7am: ')
weather = input ('Enter a weather condition, e.g sunny: ')



#build story
story = (
f'Every {day}, I {daily_routine} at {time}. \n'
f'After that, I go to the {place} with my {family}. \n'
f'My favourite colour is {colour}. \n'
f'Therefore, while driving to the {place}, I take a picture of the  {ordinal_number} {colour} building. \n'
f'Last {day}, it was {weather}, so I could not take any picture. \n'
f'My {family} said that I can take pictures in {month}, because it will not be {weather}. \n'
f'I love my {family}'
)
print (story)
