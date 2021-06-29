print('Welcome to my computer quiz!')

playing = input('Would you like to play? ')

if playing.lower() != 'yes':
    quit()

print('cool, lets play :)')
score = 0

answer = input('What does CPU stand for? ')
if answer.lower() == 'central processing unit':
    print('you got it!')
    score += 1
else: 
    print('wrong')

answer = input('What does CPU stand for? ')
if answer.lower() == 'central processing unit':
    print('you got it!')
    score += 1
else: 
    print('wrong')

answer = input('What does GPU stand for? ')
if answer.lower() == 'graphics processing unit':
    print('you got it!')
    score += 1
else: 
    print('wrong')

answer = input('What does RAM stand for? ')
if answer.lower() == 'random acess memory':
    print('you got it!')
    score += 1
else: 
    print('wrong')

answer = input('What does PSU stand for? ')
if answer.lower() == 'power supply unit':
    print('you got it!')
    score += 1
else: 
    print('wrong')

print('You got ' + str(score) + 'questions correct')
print('You got ' + str(score / 4) * 100 + '%.')