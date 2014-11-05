__author__ = 'root'
number = 23
guess = int(raw_input('Enter an interger :'))
if guess == number:
    print 'Congratulations, you guessed is.'
    print "(but you don't win any prizes!)"
elif guess < number:
    print 'No, it is a little higher than that'
else:
    print 'No, it is a little lower than that'

print 'Done'

if True:
    print 'true'