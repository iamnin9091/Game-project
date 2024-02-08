import sys
import random
from enum import Enum
class game(Enum):
    ROCK=1
    PAPER=2
    SCISSORS=3

    
playChoice = input('Enter ...\n1 --- rock🌑 ,\n2 ---paper📄, or \n3 ---scissors ✂:\n')
player = int(playChoice)

#condition set
if player < 1 | player > 3:
    sys.exit('please select with in 1-3')
computer_choice = random.choice('123')
computer = int(computer_choice)
#developing user experience
print('You chose '+str(game(player)).replace('game.','')+'.')
print('Computer chose '+str(game(computer)).replace('game.','')+'.')

#game logic
if player == 1 and computer == 3:
        print('🎉 You win')
elif player == 3 and computer == 2:
        print('🎉 You win')
elif player == 2 and computer == 1:
        print('🎉 You win')
elif player == computer:
        print('😲 tie')
else:
        print('😥 You lose')

