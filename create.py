## double cliquer sur create pour créer un fichier setup.py
## ouvrir l'invite de commande se déplacer dans le dossier
## executer la commande "pyhton setup.py build"
## build étant le nom du dossier ou va se créer l'executable



import pygame
from pygame.locals import *
import random

pygame.init()

fenetre = pygame.display.set_mode((300,300))

rectangle00 = Rect(0,0,100,100)
rectangle01 = Rect(0,100,100,100)
rectangle02 = Rect(0,200,100,100)
rectangle10 = Rect(100,0,100,100)
rectangle11 = Rect(100,100,100,100)
rectangle12 = Rect(100,200,100,100)
rectangle20 = Rect(200,0,100,100)
rectangle21 = Rect(200,100,100,100)
rectangle22 = Rect(200,200,100,100)


with open(r'.\baseDeDonnee.py','w',encoding='utf8') as f:

    f.write("import numpy as np\n\n")

    f.write("donneeEntrainement = [")
    
    while 1: 
        rand = [random.random() for i in range(9)]
        pygame.draw.rect(pygame.display.get_surface(), (255*rand[0],255*rand[0],255*rand[0]), rectangle00)
        pygame.draw.rect(pygame.display.get_surface(), (255*rand[1],255*rand[1],255*rand[1]), rectangle01)
        pygame.draw.rect(pygame.display.get_surface(), (255*rand[2],255*rand[2],255*rand[2]), rectangle02)
        pygame.draw.rect(pygame.display.get_surface(), (255*rand[3],255*rand[3],255*rand[3]), rectangle10)
        pygame.draw.rect(pygame.display.get_surface(), (255*rand[4],255*rand[4],255*rand[4]), rectangle11)
        pygame.draw.rect(pygame.display.get_surface(), (255*rand[5],255*rand[5],255*rand[5]), rectangle12)
        pygame.draw.rect(pygame.display.get_surface(), (255*rand[6],255*rand[6],255*rand[6]), rectangle20)
        pygame.draw.rect(pygame.display.get_surface(), (255*rand[7],255*rand[7],255*rand[7]), rectangle21)
        pygame.draw.rect(pygame.display.get_surface(), (255*rand[8],255*rand[8],255*rand[8]), rectangle22)

        pygame.display.flip()

        c=1
        while c:
            event = pygame.event.wait()
            if event.type == QUIT:
                pygame.display.quit()
                c=0
                t = [0,0,0,0,0,1]
                f.write(f"(np.array({rand}).reshape(9,1),np.array({t}).reshape(6,1))]\n")

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    t = [1,0,0,0,0,0]
                    c=0

                if event.key == K_DOWN:
                    t = [0,1,0,0,0,0]
                    c=0

                if event.key == K_LEFT:
                    t = [0,0,1,0,0,0]
                    c=0

                if event.key == K_RIGHT:
                    t = [0,0,0,1,0,0]
                    c=0

                if event.key == K_SPACE:
                    t = [0,0,0,0,1,0]
                    c=0

                if event.key == K_r:
                    t = [0,0,0,0,0,1]
                    c=0

                f.write(f"(np.array({rand}).reshape(9,1),np.array({t}).reshape(6,1)),\n")

