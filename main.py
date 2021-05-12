import pickle
import pygame
import sys
import random
import time

#===================   Base     =================

pygame.init()
win = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Hangman')

#===================   Variables     =============

FPS = 30
clock = pygame.time.Clock()
IMAGES = []
SOUNDS = []
running = True
used_buttons = []
guess = ''
win_word = ''
lives = 6
output = ''
r=0
put=''
game_status = 0

#================   Resources    =============

for pic in range(7):
    image = pygame.image.load('res/gfx/hangman'+str(pic+1) +'.png')
    IMAGES.append(image)

#=================   Functions   ===============

def button(center_pos, radius,margin):

    # This function draws all the alphabetical buttons on the screen. 

    # center_pos : center position of first button
    # radius : radius of button
    # margin : margin between buttons

    init_x = list(center_pos)[0]
    font = pygame.font.SysFont('Times New Roman',20)
    for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if i in used_buttons:
            list_center = list(center_pos)
            list_center[0] += (margin + 2*radius)

            if i == 'M':
                list_center[1] += (margin + 2*radius)
                list_center[0] = init_x
            center_pos = tuple(list_center)
            continue
        
        pygame.draw.circle(win,(98,200,150),center_pos,radius)       
        list_center = list(center_pos)
        win.blit(font.render(i,1,(0,0,0)),(list_center[0]-8,list_center[1]-12))
        list_center[0] += (margin + 2*radius)
        
        if i == 'M':
            list_center[1] += (margin + 2*radius)
            list_center[0] = init_x
        center_pos = tuple(list_center)

def Game_Output():

    # It draws the underscores and the 'lives remaining' on the screen.

    global guess,used_buttons,output,lives

    font2 = pygame.font.SysFont('Times New Roman',40)
    win.blit(font2.render(output,1,(0,0,0)),(260,120))

    # print('Lives remaining : ',lives)
    font3 = pygame.font.SysFont('Geogia',20)
    win.blit(font3.render((f'Lives remaining : {lives}'),1,(0,0,0)),(260,180))
    
def Choose_winning_word():

    # This function choses the winning word.

    global win_word
    
    word_Dictionary= ['demolish','bool','cancel','sand','player','favourite','fantastic','adorable','performance',
                      'cookware','infection','democracy','delicious','delight','diamond','development','devotion',
                      'diagram','diarrhoea','dictionary','different','dignity','dimension','diminish','disability',
                      'disappear','disappoint','disaster','discriminate','disobedience','displace','disposal',
                      'disqualify','dispute','dispersion','disturb','diverse','divisible','dizziness','doctor','document','dodge',
                      'dominant','file','festival','dibrous','finished','fireworks','fishing','floalting','flexible','flood',
                      'formality','forestry','forgive','fracture','fragrance','fraternity','furniture','ginger','gesture','geyser',
                      'glimmer','glossary','glory','gooseberry','guardian','guility','gymnastic']


    wining_Word_no=random.randint(0,(len(word_Dictionary)-1))
    win_word=word_Dictionary[wining_Word_no]  
    
def main():

    # This main function is responsible for the main gameloop.

    global running,output,lives,guess,r,put,game_status

    game_status = 0 # monitors the game state to blit hangman images
    used_buttons = []   # reset the used buttons to empty
    running = True  # Set running = True in this function so it can run again and again
    lives = 6   # It is 6 because hangman has 6 body parts to appear before he dies
    Choose_winning_word()
    output = '_ '*len(win_word) # changing the output variable to underscores to display
    
    side_wipe()

    # Main while loop
    while running:
        clock.tick(FPS)
        guess = ''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_animate()
                pygame.quit()
                sys.exit()
    
            # looks for all the key presses and appends in 'used buttons'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    used_buttons.append('A')
                    guess ='A'
                if event.key == pygame.K_b:
                    used_buttons.append('B')
                    guess='B'
                if event.key == pygame.K_c:
                    used_buttons.append('C')
                    guess='C'
                if event.key == pygame.K_d:
                    used_buttons.append('D')
                    guess='D'
                if event.key == pygame.K_e:
                    used_buttons.append('E')
                    guess='E'
                if event.key == pygame.K_f:
                    used_buttons.append('F')
                    guess='F'
                if event.key == pygame.K_g:
                    used_buttons.append('G')
                    guess='G'
                if event.key == pygame.K_h:
                    used_buttons.append('H')
                    guess='H'
                if event.key == pygame.K_i:
                    used_buttons.append('I')
                    guess='I'
                if event.key == pygame.K_j:
                    used_buttons.append('J')
                    guess='J'
                if event.key == pygame.K_k:
                    used_buttons.append('K')
                    guess='K'
                if event.key == pygame.K_l:
                    used_buttons.append('L')
                    guess='L'
                if event.key == pygame.K_m:
                    used_buttons.append('M')
                    guess='M'
                if event.key == pygame.K_n:
                    used_buttons.append('N')
                    guess='N'
                if event.key == pygame.K_o:
                    used_buttons.append('O')
                    guess='O'
                if event.key == pygame.K_p:
                    used_buttons.append('P')
                    guess='P'
                if event.key == pygame.K_q:
                    used_buttons.append('Q')
                    guess='Q'
                if event.key == pygame.K_r:
                    used_buttons.append('R')
                    guess='R'
                if event.key == pygame.K_s:
                    used_buttons.append('S')
                    guess='S'
                if event.key == pygame.K_t:
                    used_buttons.append('T')
                    guess='T'
                if event.key == pygame.K_u:
                    used_buttons.append('U')
                    guess='U'
                if event.key == pygame.K_v:
                    used_buttons.append('V')
                    guess='V'
                if event.key == pygame.K_w:
                    used_buttons.append('W')
                    guess='W'
                if event.key == pygame.K_x:
                    used_buttons.append('X')
                    guess='X'
                if event.key == pygame.K_y:
                    used_buttons.append('Y')
                    guess='Y'
                if event.key == pygame.K_z:
                    used_buttons.append('Z')        
                    guess='Z'        
        
        
        win.fill((255,255,255))
        win.blit(IMAGES[game_status],(30,30))
    

        button((35,280),16,12)
        Game_Output()


        r=0
        put=''
        if guess != '':
            if (guess == used_buttons[-1]) and (guess not in used_buttons[0:-1]):
                guess = guess.lower()
                if guess in win_word:
                    for i in output:
                        if i != ' ':
                            if guess== win_word[r]:
                                put+=guess
                            else:
                                put+=i
                            
                            r+=1
                            output=put
                        else:
                            put+=' '
                            output = put
                        
                else:
                    
                    lives-=1
                    game_status+=1
        
        if '_ ' not in output:
            
            # print(f'You Won!!!\nYou got it right..  The winning word was "{win_word.title()}"')
            running = False
            wait('win')
        
        if lives==0:
            # print(f'Sorry but You LOST....\nThe winning word was "{win_word.title()}"')
            running = False
            wait('lose')
        

        pygame.display.flip()
        pygame.display.update()
      
def wait(status):

    # this draws the end screen 
    
    # FONTS
    font = pygame.font.SysFont('Comic Sans MS',30,True)
    font2 = pygame.font.SysFont('Harlow Solid',40)
    font3 = pygame.font.SysFont('Matura MT Script Capitals',28)
    while True:
        m_pos = pygame.mouse.get_pos()
        pygame.draw.rect(win,(64,0,64),(100,80,400,240))        # outer black border
        pygame.draw.rect(win,(0,128,192),(110,90,380,220))      # inner rectangle
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (m_pos[0]>= 155 and m_pos[1]>= 225) and (m_pos[0]<= 255 and m_pos[1]<= 275):
                    main()
                if (m_pos[0]>= 345 and m_pos[1]>= 225) and (m_pos[0]<= 445 and m_pos[1]<= 275):
                    end_animate()
                    pygame.quit()
                    sys.exit()
        
        # button animation
        if (m_pos[0]>= 155 and m_pos[1]>= 225) and (m_pos[0]<= 255 and m_pos[1]<= 275):
            pygame.draw.rect(win,(240,240,120),(152,222,106,56))
            win.blit(font.render('Replay',1,(13,145,19)),(160,225))
                
        elif (m_pos[0]>= 345 and m_pos[1]>= 225) and (m_pos[0]<= 445 and m_pos[1]<= 275):
            pygame.draw.rect(win,(240,240,120),(342,222,106,56))
            win.blit(font.render('Exit',1,(204,0,5)),(362,225))
            
        else:
            pygame.draw.rect(win,(0,0,0),(150,220,110,60))          # button 1 outer border
            pygame.draw.rect(win,(240,240,120),(155,225,100,50))    # button 1 inner part
            pygame.draw.rect(win,(0,0,0),(340,220,110,60))          # button 2 outer
            pygame.draw.rect(win,(240,240,120),(345,225,100,50))    # button 2 inner        
            win.blit(font.render('Replay',1,(13,145,19)),(160,225))
            win.blit(font.render('Exit',1,(204,0,5)),(362,225))
        
        
        
        # if win
        if status == 'win':
            win.blit(IMAGES[game_status],(30,30))
            win.blit(font2.render('You WON!!',1,(204,0,5)),(182, 105))
            win.blit(font3.render('You guessed the right word.',1,(120,200,125)),(162, 173))
        
        # if lose
        if status == 'lose':
            win.blit(IMAGES[6],(30,30))
            win.blit(font2.render('You LOSE !!',1,(204,0,5)),(220, 105))
            win.blit(font3.render('You guessed the wrong word.',1,(120,200,125)),(210, 173))
            win.blit(font3.render((f'The correct word was {win_word}.'),1,(120,200,125)),(175, 193))

            

        pygame.display.update()

def start_animate():
    font = pygame.font.SysFont('Comic Sans MS',30,True)
    font2 = pygame.font.SysFont('Lucida Calligraphy',60)
    for y_axis in range(0,600):
        time.sleep(0.001)
        pygame.draw.rect(win,(48,90,0),(0,0,600,y_axis))
        if y_axis>125:
            win.blit(font.render('Welcome to ',1,(204,0,5)),(200, 105))
        if y_axis>240:
            win.blit(font2.render('HANGMAN',1,(0,0,200)),(100,200))
        pygame.display.update()

def end_animate():
    for y_axis in range(0,400):
        time.sleep(0.001)
        pygame.draw.rect(win,(48,90,80),(0,0,600,y_axis))
        pygame.display.update()

def side_wipe():
    for x in range(0,600):
        time.sleep(0.001)
        pygame.draw.rect(win,(48,160,80),(0,0,x,400))
        pygame.display.update()

#==================  Mainloop    =================

start_animate()
main()
        