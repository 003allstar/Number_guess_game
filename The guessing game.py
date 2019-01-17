import random

high_number = 30
answer = random.randint(1, high_number)
times_run = 0
guess = int(input('I am thinking of a number between 1-{}.'
                  'What is your guess:'.format(high_number)))

while times_run < 4:
    if guess != answer:
        if guess < answer:
            print('Your guess is too low. Guess higher.')
            guess = int(input('What is your next guess:'))
            times_run += 1
        else:
            print('Your guess is too high. Guess lower.')
            guess = int(input('What is your next guess:'))
            times_run += 1
    else:
        print('You got it.')
        break
else:
    print("You didn't get it. The number is {}.".format(answer))
