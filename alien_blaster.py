import pygame,sys,random,math
pygame.init()

scrwid=500
scrhei=500
spacex=scrwid/2
spacey=scrhei-102
vel=5
flag=0
blast=False
score=0
gameover=False

clock=pygame.time.Clock()



bg=pygame.image.load("space-blaster-pygame-master/bg.png")
ship=pygame.image.load("space-blaster-pygame-master/ship.png")
alien=pygame.image.load("space-blaster-pygame-master/enemy.png")
bomb=pygame.image.load("space-blaster-pygame-master/expl.png")

black=(0,0,0)
white=(255,255,255)
yellow=(255,255,0)
blue=(0,0,255)

win=pygame.display.set_mode((scrwid,scrhei))
pygame.display.set_caption("Alien Blaster")
win.blit(bg,(0,0))

def start():
      win.blit(bg,(0,0))
      pygame.draw.rect(win, white , pygame.Rect(150, 100, 200, 60),2)
      pygame.draw.rect(win, white , pygame.Rect(150, 220, 200, 60),2)
      myfont=pygame.font.SysFont('comicsansms',37)
      txtsurf=myfont.render("START",True,(255,255,255),(0,0,0))
      win.blit(txtsurf,(185,105))
      txtsurf=myfont.render("EXIT",True,(255,255,255),(0,0,0))
      win.blit(txtsurf,(200,225))
      pygame.display.update()
      for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            x,y=pygame.mouse.get_pos()
            print(x,y)
            if((x>150 and x<350)and(y>100 and y<160)):
                print("Start")
                return
            if((x>150 and x<350)and(y>220 and y<280)):
                print("Exiting")
                pygame.quit()
                sys.exit()
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
      start()


def gameover():
    win.blit(bg,(0,0))
    mifont=pygame.font.SysFont('comicsansms',48)
    sur=mifont.render("GAME OVER",False,(255,255,255),(0,0,0))
    win.blit(sur,(100,200))

    mofont=pygame.font.SysFont('comicsansms',40)
    la=mofont.render("Score :",False,(255,255,255),(0,0,0))
    win.blit(la,(200,300))

    ola=mofont.render(str(score),False,(255,255,255),(0,0,0))
    win.blit(ola,(350,300))
    
    pygame.display.flip()

aliens_x=[]
aliens_y=[]

for i in range(0,7):
    g=random.randint(5,160)
    aliens_x.append(g)
    h=random.randint(5,100)
    aliens_y.append(h)
    
    

def redraw():

    for bullet in bullets:
            bullet.draw(win)
    myfont=pygame.font.SysFont('comicsansms',15)
    txtsurf=myfont.render("SCORE:",False,(255,255,255),(0,0,0))
    surf=myfont.render(str(score),False,(255,255,255),(0,0,0))
    draw=myfont.render("time: ",False,(255,255,255),(0,0,0))
    timedraw=myfont.render(str(30-round(seconds)),False,(255,255,255),(0,0,0))
    win.blit(txtsurf,(0,470))
    win.blit(surf,(100,470))
    win.blit(draw,(0,0))
    win.blit(timedraw,(50,0))
    pygame.display.update()
           
    win.blit(bg,(0,0))
    win.blit(ship,(spacex,spacey))
    for i in range(0,len(aliens_x)):
         print(aliens_x,aliens_y)
         win.blit(alien,((aliens_x[i])*2.5,(aliens_y[i])*2.5))
         if blast :  
            
            win.blit(bomb,((aliens_x[i])*2.5,(aliens_y[i])*2.5))
   
            
        
    pygame.display.update()
def alienblast(i):
    win.blit(bomb,((aliens_x[i])*2.5,(aliens_y[i])*2.5))
    aliens_x.pop(i)
    aliens_y.pop(i)
    pygame.display.update()


class shoot:
    def __init__(self,x,y,radius,colour):
        self.x=x
        self.y=y
        self.radius=radius
        self.colour=colour
        self.velocity=10
    def draw(self,window):
        pygame.draw.circle(window,self.colour,(self.x,self.y),self.radius)
    

def space_ship(a):
    win.blit(bg,(0,0))
    if a==0:
        global spacex
        spacex=spacex-vel
        
        pygame.display.update()
        if spacex>398:
            spacex=398
        if spacex<0:
            spacex=0
    if a==1:
    
        spacex=spacex+vel

        
        pygame.display.update()
        if spacex>398:
            spacex=398
        if spacex<0:
            spacex=0

run=True
bullets=[]

start()
start_ticks=pygame.time.get_ticks()
while run:
    clock.tick(100)
    flag=0
    seconds=(pygame.time.get_ticks()-start_ticks)/1000 
    if seconds<30:
          
            if(len(aliens_x)<7):
               print("Adding")
               aliens_x.append(random.randint(5,160))
               aliens_y.append(random.randint(5,100))
         
                    
            for bullet in bullets:
                blast=False
                j=len(aliens_x)
                for i in range(0,j):
                    try:
                     if ((bullet.x>=(aliens_x[i]*2.5) and bullet.x<=(aliens_x[i]*2.5)+45) and (bullet.y>=(aliens_y[i]*2.5) and bullet.y<=(aliens_y[i]*2.5)+45)):
                        
                         alienblast(i)
                         print(len(aliens_x))
                         print(i) 
                         score+=1
                    except:
                        pass
            for bullet in bullets:
                if bullet.y>0:
                    bullet.y-=bullet.velocity
                else:
                    bullets.remove(bullet)

            keys=pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                flag=1
                if len(bullets)<10:
                    bullets.append(shoot(round(spacex+37),round(spacey),5,white))

            if keys[pygame.K_LEFT] and flag==0:
            
                space_ship(0)
            

            if keys[pygame.K_RIGHT] and flag==0:
                flag=0
                space_ship(1)
            def run(self):
             if self.shoot.collideWithBullet():
                 print("Game Over")
            redraw()
    else:
         gameover()
    

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
                

        
        

        
        

    

        
        
        
    





