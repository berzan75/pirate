import pygame
import time 
import random
from pygame.locals import *

pygame.init()
pygame.display.set_caption("pirate")
WIDTH=900
HEIGHT=700

s=pygame.display.set_mode([WIDTH,HEIGHT])

def change_background(img):
    background= pygame.image.load(img)
    bg=pygame.transform.scale(background, (WIDTH, HEIGHT))
    s.blit(bg,(0,0))
    

class Pirate(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("pirate.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(40,40))
        self.rect=self.image.get_rect()

class Good(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image=pygame.image.load(img).convert_alpha()
        self.image=pygame.transform.scale(self.image,(40,40))
        self.rect=self.image.get_rect()

class no(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("peter.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(40,40))
        self.rect=self.image.get_rect()

good=["parrot.png","chest.png","ship.png"]

pirate_list= pygame.sprite.Group()
peter_list = pygame.sprite.Group()
allsprites = pygame.sprite.Group()

#creating recyclable items
for i in range (50):
    item=Good(random.choice(good))
    item.rect.x = random.randrange(WIDTH)
    item.rect.y = random.randrange(HEIGHT)
    pirate_list.add(good)
    allsprites.add(good)

for i in range (50):
    p=no()
    p.rect.x = random.randrange(WIDTH)
    p.rect.y = random.randrange(HEIGHT)
    peter_list.add(p)
    allsprites.add(p)

pirate= Pirate()
allsprites.add(bin)

WHITE= (255,255,255)

playing=True
score=0
clock=pygame.time.Clock()
start_time= time.time()

myfont=pygame.font.SysFont("Times New Roman",30)
timing=pygame.font.SysFont("Times New Roman",20)
text=myfont.render("Score ="+str(score),True,WHITE)

while playing:
    clock.tick(60)

    time_elapsed = time.time()-start_time()
    if time_elapsed > 60:
        if score > 40:
            text=myfont.render("you won")
        else:
            text=myfont.render("better luck next time")
            text=timing.render("time_elapsed:"+str(60-int(time_elapsed)),True,WHITE)
        s.blit(text,(10,10))
    
        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if pirate.rect.y>0:
                pirate.rect.y-=5
        if keys[pygame.K_DOWN]:
            if pirate.rect.y<690:
                pirate.rect.y+=6
        if keys[pygame.K_LEFT]:
            if pirate.rect.x>0:
                pirate.rect.x-=5
        if keys[pygame.K_RIGHT]:
            if pirate.rect.x<890:
                pirate.rect.x+=5
        
        pirate_hit_list=pygame.sprite.spritecollide(pirate, pirate_list,True)
        peter_hit_list=pygame.sprite.spritecollide(pirate,peter_list,True)

        for i in pirate_hit_list:
            score+=1
            text=myfont.render("score:"+str(score),True,WHITE)
        
        for i in peter_list:
            score-=5
            text=myfont.render("score:"+str(score),True,WHITE)
        s.blit(text,(10,690))

        allsprites.draw(s)
        
    pygame.display.update()
pygame.quit()