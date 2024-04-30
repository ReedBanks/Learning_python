from datetime import datetime
import random

time=datetime.now().hour
name=input("Name : ")

# checking time for greeting 
if time < 12 :
    print(f'Good Morning, {name}')
elif time < 16 :
    print(f'Good Afternoon, {name}')
else :
    print(f'Good Evening, {name}')

wordlist=['hacke','bounty','rand']
displayword=[]
#random selection/choosing from wordlist
choosen_word=random.choice(wordlist)
#guess letter
guess=print(input("Guess a letter: ").lower())
print(f'chosen word : {choosen_word}')

for letter in choosen_word:
   if letter == guess:
       print(f'guess is right')
   else:
       print(f'guess is wrong')


''' this is a comment '''
