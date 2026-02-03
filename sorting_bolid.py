# started points

ferrari = 0
mclaren = 0
mercedes = 0
red_bull = 0

print('=================================================================================================================')
print('Welcome to the Sorting Bolid Quiz! Answer the following questions to find out which Formula 1 team you belong to.')
print('=================================================================================================================')

# Question 1

print('What is your favorite color?')
print(' 1) Red')
print(' 2) Orange')
print(' 3) Black')
print(' 4) Blue')

answer = int(input('Enter answer (1-4): '))

if answer == 1:
    ferrari = ferrari + 1
elif answer == 2:
    mclaren = mclaren + 1
elif answer == 3:
    mercedes = mercedes + 1
elif answer == 4:
    red_bull = red_bull + 1
else:
    print('Invalid answer. Please enter a number between 1 and 4.')


# Question 2

print('What is your favourite country?')
print(' 1) Italy')
print(' 2) UK')
print(' 3) Germany')
print(' 4) Austria')

answer = int(input('Enter answer (1-4): '))

if answer == 1:
    ferrari = ferrari + 2
elif answer == 2:
    mclaren = mclaren + 2
elif answer == 3:
    mercedes = mercedes + 2
elif answer == 4:
    red_bull = red_bull + 2
else:
    print('Invalid answer. Please enter a number between 1 and 4.')


# Question 3

print('What is your favourite driver?')
print(' 1) Charles Leclerc')
print(' 2) Lando Norris')
print(' 3) George Russell')
print(' 4) Max Verstappen')

answer = int(input('Enter answer (1-4): '))

if answer == 1:
    ferrari = ferrari + 3
elif answer == 2:
    mclaren = mclaren + 3
elif answer == 3:
    mercedes = mercedes + 3
elif answer == 4:
    red_bull = red_bull + 3
else:
    print('Invalid answer. Please enter a number between 1 and 4.')


# Question 4

print('What is your favourite animal?')
print(' 1) Ladybug')
print(' 2) Tiger')
print(' 3) Puma')
print(' 4) Dolphin')

answer = int(input('Enter answer (1-4): '))

if answer == 1:
    ferrari = ferrari + 4
elif answer == 2:
    mclaren = mclaren + 4
elif answer == 3:
    mercedes = mercedes + 4
elif answer == 4:
    red_bull = red_bull + 4
else:
    print('Invalid answer. Please enter a number between 1 and 4.')


# Final Calculation
print('Your scores are as follows:')
print(' Ferrari: ', ferrari)
print(' McLaren: ', mclaren)
print(' Mercedes: ', mercedes)
print(' Red Bull: ', red_bull)