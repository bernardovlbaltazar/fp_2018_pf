from functions import *
from sprites import *
import pygame
import sys


x = 800
y = 600
aux=False
continua = False
pauseMusic = False
screenSize(x,y,None,None,False)
setBackgroundImage("opening image/opening image.jpg")
makeMusic("soundtracks/chill_discover.wav")
ingameMusic = makeSound("soundtracks/int_discover.wav")
playMusic(-1)

class Player:
    def __init__(self,name):

        self.x = 50
        self.y = 200
        self.resources=[]
        self.speedAnimation = 100
        self.speed=1
        self.image=0
        self.count=0
        self.count1=0
        self.warning=False
        self.name=name

    def animationRight(self,sprite,nextFrame):
        
        if clock() > nextFrame:
            self.image+=1
            if self.image >4:
                self.image=0
            changeSpriteImage(sprite,self.image)
            nextFrame = clock() + self.speedAnimation
        self.x += self.speed
        return nextFrame

    
    def animationJumpMovRight(self,sprite,nextFrame):
                                                    
        if clock() > nextFrame:                       
            self.image+=1                             
            if self.image >4:                         
                self.image=0                          
            changeSpriteImage(sprite,self.image)      
            nextFrame = clock() + self.speedAnimation
        
        self.x += self.speed*1.1
        return nextFrame


    def animationLeft(self,sprite,nextFrame):
        if clock() > nextFrame:
            self.image+=1
            if self.image >4:
                self.image=0
            changeSpriteImage(sprite,self.image)
            nextFrame = clock() + self.speedAnimation
        self.x -= self.speed
        return nextFrame

    def animationJumpMovLeft(self,sprite,nextFrame):
                                                    
        if clock() > nextFrame:                       
            self.image+=1                             
            if self.image >4:                         
                self.image=0                          
            changeSpriteImage(sprite,self.image)      
            nextFrame = clock() + self.speedAnimation
        
        self.x -= self.speed*1.1
        return nextFrame
    
    def animationDown(self,sprite,nextFrame):
        if clock() > nextFrame:
            self.image+=1
            if self.image >2:
                self.image=0
            changeSpriteImage(sprite,self.image)
            nextFrame = clock() + self.speedAnimation
        self.y += self.speed
        return nextFrame

    def animationUp(self,sprite,nextFrame):
        if clock() > nextFrame:
            self.image+=1
            if self.image >2:
                self.image=0
            changeSpriteImage(sprite,self.image)
            nextFrame = clock() + self.speedAnimation
        self.y -= self.speed
        return nextFrame

class Adereco:
    def __init__(self,x,y,hitbX,hitbY):    
        self.x = x
        self.y = y
        self.hitboxX = hitbX
        self.hitboxY = hitbY
        self.hit = False
        self.count=0
        self.nextFrame=0
        self.image=0
        self.speedAnimation = 80
        self.looplimit = 14
        

    def animate(self,sprite):

        if clock() > self.nextFrame:
            self.image+=1
            if self.image > self.looplimit:
                self.image=0
            changeSpriteImage(sprite,self.image)
            self.nextFrame = clock() + self.speedAnimation        
        
        

class AderecoMovel:
    def __init__(self,x,y):#botClass.x-30,botClass.y-25,65,50
        self.x = x
        self.y = y
        self.hitboxX= range(self.x - 30 , self.x + 35 )
        self.hitboxY= range(self.y - 25 , self.y + 25 )
        self.hit = False
        self.image=0
        self.speed = .2
        self.speedAnimation = 300
        self.path=500
        self.loopimage = 6
        self.nextFrame=0
        self.count=0

    def move(self,mode,sprite,nextFrame):
        self.hitboxX= range(int(self.x) - 50 , int(self.x) + 35 )
        self.hitboxY= range(int(self.y) - 60 , int(self.y) + 25 )
        
        if mode == 1 and self.speed>0: #horizontal move
            if self.x + self.speed < self.path:
                self.x += self.speed
            else:
                self.speed *= -1
                self.path-=200
        elif self.speed<=0 and mode == 1:
            if self.x - self.speed > self.path:
                self.x += self.speed
            else:
                self.speed *= -1
                self.path+=200

        if mode == 2 and self.speed>0: #vertical move
            if self.y + self.speed < self.path:
                self.y += self.speed
            else:
                self.speed *= -1
        elif self.speed<=0 and mode == 2:
            if self.y - self.speed > self.path:
                self.y += self.speed
            else:
                self.speed *= -1
        return nextFrame

                
        
        
    
#main colision    
def colision(plyr,objeto,hit,warn): #needs x , y , hitboxX, hitboxY defitions by the class

    
    if plyr.x in objeto.hitboxX and plyr.y in objeto.hitboxY:
            hit= True
            if 0<plyr.x<800 and 0<=plyr.y<600:
                if plyr.x < objeto.x:
                    plyr.x -= 1
                else:
                    plyr.x += 1
                    
                if plyr.y < objeto.y - 30:
                    plyr.y -= 1

                else:
                    plyr.y += 1
            else:
                plyr.y=240
                plyr.x=100
                warn=True
    return hit ,warn
    
   

#Class manage

player = Player("jorge")
skeleton = Adereco(500,500,range(500 - 45 , 500 + 15 ),range(500 - 60 , 500 ))
botClass = AderecoMovel(700,250)
tree = Adereco(111,402,range(111 - 100 , 111 + 70 ),range(402 - 100 , 402 + 30 ))
tree2 = Adereco(660,465,range(660 - 100 , 660 + 70 ),range(465 - 110 , 465 + 30 ))
tree3 = Adereco(740,30,range(740 - 100 , 740 + 70 ),range(30 - 100 , 30 + 30 ))
tree2.speedAnimation = 110
tree3.speedAnimation = 140

#^^Class manage^^

#pre_data
nextFrame = clock()
hideTextBox(playertalk)
hideTextBox(bottalk)
hideTextBox(alienhead)
hideTextBox(leave)
hideTextBox(warning)
hideTextBox(wild)







while True:
    
    
    if not continua:
        
        if mousePressed() :
        
            setBackgroundImage("sprite sheets/map/mars map pixel.jpg")
            stopMusic()
            playSound(ingameMusic,-1)
            continua = True
        
    else:

        if player.count<1:
            #player
            showSprite(playerDown)
            #trees
            showSprite(treeSprite)
            showSprite(treeSprite2)
            showSprite(treeSprite3)
            moveSprite(treeSprite,tree.x,tree.y,True)
            moveSprite(treeSprite2,tree2.x,tree2.y,True)
            moveSprite(treeSprite3,tree3.x,tree3.y,True)
            #skeleton
            showSprite(alienSkeleton)
            moveSprite(alienSkeleton,skeleton.x,skeleton.y,True)
            showSprite(alienSkeleton)
            #bot
            showSprite(bot)
            
            player.count+=1

        #player dangerous area
        player.warning=False
        
        #skeletonHit
        skeleton.hit = False
        
        #colision_skeleton
        skeleton.hit,player.warning = colision(player,skeleton,skeleton.hit,player.warning)
        

        #bot
        botClass.hit = False
        #botClass.move(1,bot,nextFrame)
        if clock() > botClass.nextFrame:
            botClass.image+=1
            if botClass.image >6:
                botClass.image=0
            changeSpriteImage(bot,botClass.image)
            botClass.nextFrame = clock() + 600
        botClass.move(1,bot,botClass.nextFrame)
        moveSprite(bot,botClass.x,botClass.y,True)
        

        #colision_bot
        botClass.hit,player.warning = colision(player,botClass,botClass.hit,player.warning)

        #treesHit and animate
        tree.hit = False
        tree2.hit = False
        tree3.hit = False
        tree.animate(treeSprite)
        tree2.animate(treeSprite2)
        tree3.animate(treeSprite3)
        

        #colision_tree
        
        tree.hit,player.warning = colision(player,tree,tree.hit,player.warning)
        tree2.hit,player.warning = colision(player,tree2,tree2.hit,player.warning)
        tree3.hit,player.warning = colision(player,tree3,tree3.hit,player.warning)

        

        
        #controlos
        if keyPressed("e") :
            moveSprite(yesOption,560,270)
            moveSprite(noOption,180,270)
            showSprite(pauseScreen)
            showSprite(yesOption)
            showSprite(noOption)
            aux=True
    
        elif aux:
            
            if spriteClicked(yesOption):
                break
            elif spriteClicked(noOption):
                hideSprite(pauseScreen)
                killSprite(yesOption)
                killSprite(noOption)
                aux=False

        elif keyPressed("right") and not skeleton.hit and not botClass.hit and not tree.hit and not tree2.hit and not tree3.hit and 770 > player.x :
            
            
            if keyPressed("space") and not skeleton.hit:
                showSprite(playerJumpRight)
                hideSprite(playerRight)
                hideSprite(playerLeft)
                hideSprite(playerDown)
                hideSprite(playerUp)
                hideSprite(playerJumpLeft)
                nextFrame = player.animationJumpMovRight(playerJumpRight,nextFrame)
               
           # else:
            
            showSprite(playerRight)
            hideSprite(playerLeft)
            hideSprite(playerDown)
            hideSprite(playerUp)
            hideSprite(playerJumpRight)
            hideSprite(playerJumpLeft)
            nextFrame = player.animationRight(playerRight,nextFrame)
            moveSprite(playerRight,player.x,player.y)

        elif keyPressed("left") and not skeleton.hit and not botClass.hit and not tree.hit and not tree2.hit and not tree3.hit and 0< player.x:

            showSprite(playerLeft)
            hideSprite(playerRight)
            hideSprite(playerDown)
            hideSprite(playerUp)
            hideSprite(playerJumpRight)
            hideSprite(playerJumpLeft)
            nextFrame = player.animationLeft(playerLeft,nextFrame)
            moveSprite(playerLeft,player.x,player.y)

        elif keyPressed("down") and not skeleton.hit and not botClass.hit and not tree.hit and not tree2.hit and not tree3.hit and player.y<560:
            
            showSprite(playerDown)
            hideSprite(playerLeft)
            hideSprite(playerRight)
            hideSprite(playerUp)
            hideSprite(playerJumpRight)
            hideSprite(playerJumpLeft)
            nextFrame = player.animationDown(playerDown,nextFrame)
            moveSprite(playerDown,player.x,player.y)

        elif keyPressed("up") and not skeleton.hit and not botClass.hit and not tree.hit and not tree2.hit and not tree3.hit and player.y>0:
            
            showSprite(playerUp)
            hideSprite(playerLeft)
            hideSprite(playerDown)
            hideSprite(playerRight)
            hideSprite(playerJumpRight)
            hideSprite(playerJumpLeft)
            nextFrame = player.animationUp(playerUp,nextFrame)
            moveSprite(playerUp,player.x,player.y)

        else:
            player.image = 0
            changeSpriteImage(playerRight,player.image)
            changeSpriteImage(playerLeft,player.image)
            changeSpriteImage(playerUp,player.image)
            changeSpriteImage(playerDown,player.image)
            changeSpriteImage(playerJumpRight,3)
            changeSpriteImage(playerJumpLeft,3)
            moveSprite(playerRight,player.x,player.y)
            moveSprite(playerLeft,player.x,player.y)
            moveSprite(playerDown,player.x,player.y)
            moveSprite(playerUp,player.x,player.y)

        if skeleton.hit and skeleton.count<1:
            showTextBox(leave)
            showTextBox(alienhead)
            hideTextBox(bottalk)
            hideTextBox(playertalk)
            hideTextBox(warning)
            hideTextBox(wild)
            skeleton.count+=1
            tree.count=0
            tree2.count=0
            botClass.count=0
            player.count1=0

        elif botClass.hit and botClass.count<1:
            showTextBox(bottalk)
            hideTextBox(alienhead)
            hideTextBox(playertalk)
            hideTextBox(warning)
            hideTextBox(wild)
            botClass.count+=1
            tree.count=0
            tree2.count=0
            player.count1=0
            skeleton.count=0
        elif tree.hit and tree.count<1:
            showTextBox(playertalk)
            hideTextBox(bottalk)
            hideTextBox(alienhead)
            hideTextBox(warning)
            hideTextBox(wild)
            tree.count+=1
            tree2.count=0
            skeleton.count=0
            player.count1=0
            botClass.count=0
        elif player.warning and player.count1<1:
            showTextBox(warning)
            hideTextBox(playertalk)
            hideTextBox(bottalk)
            hideTextBox(alienhead)
            hideTextBox(wild)
            player.count1+=1
            tree.count = 0
            tree2.count=0
            skeleton.count=0
            botClass.count=0
        elif tree2.hit and tree2.count<1:
            showTextBox(wild)
            hideTextBox(playertalk)
            hideTextBox(bottalk)
            hideTextBox(alienhead)
            hideTextBox(warning)
            tree2.count+=1
            tree.count = 0
            player.count1=0
            skeleton.count=0
            botClass.count=0

    
        
        
        
end()        
        

