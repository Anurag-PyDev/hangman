import time
import random

##===========================================================

time.sleep(1)
print('''Welcome to HANGMAN !!!!

Let's start the game..
''')
time.sleep(0.5)

NAME = input("What's Your Name Player : ").title()
time.sleep(0.5)
print(f'WELCOME {NAME} Lets start.....\n\n')
time.sleep(0.5)

##==================     VARIABLES  ++++++++++++++++++++++++++

guess=''
guessed_letters=''
win_word=''
put=''
r=0

#=======================================================
turns=int(input(f'How many turns do you want {NAME} (3-15) : '))
print('\n')

def Game_Output():
    global guess,guessed_letters,output
    print(output)
    print('Lives remaining : ',turns)
    guess=input('Guess a letter : ')
    guessed_letters+=' '+guess
    

def Choose_winning_word():
    global win_word

    
    word_Dictionary= ['demolish','sand','player','favourite','fantastic','adorable','performance',
                      'cookware','infection','democracy','delicious','delight','diamond','development','devotion',
                      'diagram','diarrhoea','dictionary','different','dignity','dimension','diminish','disability',
                      'disappear','disappoint','disaster','discriminate','disobedience','displace','disposal',
                      'disqualify','dispute','dispersion','disturb','diverse','divisible','dizziness','doctor','document','dodge',
                      'dominant','file','festival','dibrous','finished','fireworks','fishing','floalting','flexible','flood',
                      'formality','forestry','forgive','fracture','fragrance','fraternity','furniture','ginger','gesture','geyser',
                      'glimmer','glossary','glory','gooseberry','guardian','guility','gymnastic']


    wining_Word_no=random.randint(0,(len(word_Dictionary)-1))
    win_word=word_Dictionary[wining_Word_no]


#============================   MAIN FUNCTIONING  =============================
if turns >= 3 and turns <= 15:
    Choose_winning_word()
    output='#'*len(win_word)
    
    while turns>0:
        Game_Output()
        r=0
        put=''
        if guess in win_word:
            for i in output:
                if guess== win_word[r]:
                    put+=guess
                else:
                    put+=i
                r+=1
                output=put
        else:
            print('The letter you guessed is not in the word.')
            turns-=1
        if '#' not in output:
            print(output)
            print(f'You Won!!!\nYou got it right..  The winning word was "{win_word.title()}"')
            break
    if turns==0:
        print(f'Sorry but You LOST....\nThe winning word was "{win_word.title()}"')
    print('Thank You for playing.....\nThis game was created by ANURAG SHARMA.')
    print('\n\n')
else:
    print('The no. of turns you entered is not allowed...')
        
            
        
    


