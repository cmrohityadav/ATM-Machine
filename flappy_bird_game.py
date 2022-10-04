'''
Author:Rohit Chhabiraj Yadav
Email:cmrohityadav23@gmail.com
'''
import pygame
x=pygame.init()
print(x)
#Game ka window
gameWindow=pygame.display.set_mode((500,500))
pygame.display.set_caption("My first Game")

#game specific variable
exit_game=False
game_over=False


#creating a game loop
while not exit_game:
    # pass

    for event in pygame.event.get():

        # print(event)
        if event.type==pygame.QUIT:
            exit_game=True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                print("You enter right arrow key")
pygame.quit()
quit()
