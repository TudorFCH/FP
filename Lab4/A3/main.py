import random
from ui import menu

#1=Rock
#2=Paper
#3=Scissors

def rps():
    print(menu())
    rounds=0
    playerwins=0
    computerwins=0
    list = [1, 2, 3]
    while rounds<3:
        rounds+=1
        computerchoice=random.choice(list)
        if(computerchoice==1):
            strcomputerchoice="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
        if(computerchoice==2):
            strcomputerchoice="""
     _______
---'    ___)___
           ______)
          _______)
         _______)
---.__________)
"""
        if(computerchoice==3):
            strcomputerchoice="""
    _______
---'   ___)___
          ______)
       __________)
      (____)
---.__(___)
"""
        playerchoice = opt = int(input('opt= '))

        if (playerchoice == 1):
            strplayerchoice = """
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """
        if (playerchoice == 2):
            strplayerchoice = """
             _______
        ---'    ___)___
                   ______)
                  _______)
                 _______)
        ---.__________)
        """
        if (playerchoice == 3):
            strplayerchoice = """
            _______
        ---'   ___)___
                  ______)
               __________)
              (____)
        ---.__(___)
        """

        print('You chose:' + str(strplayerchoice))
        print('Computer chose:' + str(strcomputerchoice))
        if((playerchoice==1 and computerchoice==3) or (playerchoice==2 and computerchoice==1) or (playerchoice==3 and computerchoice==2)):
            print('You won the round')
            playerwins+=1
            print('Score:\n' + 'PLA  ' + str(playerwins) + ':' + str(computerwins) + '  COM' )
        if((playerchoice==1 and computerchoice==2) or (playerchoice==2 and computerchoice==3) or (playerchoice==3 and computerchoice==1)):
            print('Computer won the round')
            computerwins+=1
            print('Score:' + 'PLA  ' + str(playerwins) + ':' + str(computerwins) + '  COM')
        if ((playerchoice == 1 and computerchoice == 1) or (playerchoice == 2 and computerchoice == 2) or (playerchoice == 3 and computerchoice == 3)):
            print('It is a draw')
            print('Score:' + 'PLA  ' + str(playerwins) + ':' + str(computerwins) + '  COM')

    if(playerwins>computerwins):
        print('Congrats! You won the game!')
    if(playerwins<computerwins):
        print('Unlucky... You lost the game...')
    if(playerwins==computerwins):
        print('How boring, a draw...')

rps()