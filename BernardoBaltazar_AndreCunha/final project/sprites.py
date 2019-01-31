import pygame
from functions import *


#menu
screenSize(800,600,None,None,False)
pauseScreen = makeSprite("opening image/esc/leavequestion.png")
yesOption = makeSprite("opening image/esc/yes.jpg")
noOption = makeSprite("opening image/esc/no.jpg")


#player
#right
playerRight = makeSprite("sprite sheets/player/stand/1.png")
addSpriteImage(playerRight,"sprite sheets/player/run/right/1.png")
addSpriteImage(playerRight,"sprite sheets/player/run/right/2.png")
addSpriteImage(playerRight,"sprite sheets/player/run/right/3.png")
addSpriteImage(playerRight,"sprite sheets/player/run/right/4.png")
#jumpright
playerJumpRight = makeSprite("sprite sheets/player/jump/right/1.png")
addSpriteImage(playerJumpRight,"sprite sheets/player/jump/right/2.png")
addSpriteImage(playerJumpRight,"sprite sheets/player/jump/right/3.png")
addSpriteImage(playerJumpRight,"sprite sheets/player/jump/right/4.png")
addSpriteImage(playerJumpRight,"sprite sheets/player/jump/right/5.png")
#down
playerDown = makeSprite("sprite sheets/player/stand/2.png")
addSpriteImage(playerDown,"sprite sheets/player/run/down/1.png")
addSpriteImage(playerDown,"sprite sheets/player/run/down/2.png")
#left
playerLeft = makeSprite("sprite sheets/player/stand/3.png")
addSpriteImage(playerLeft,"sprite sheets/player/run/left/1.png")
addSpriteImage(playerLeft,"sprite sheets/player/run/left/2.png")
addSpriteImage(playerLeft,"sprite sheets/player/run/left/3.png")
addSpriteImage(playerLeft,"sprite sheets/player/run/left/4.png")
#jumpleft
playerJumpLeft = makeSprite("sprite sheets/player/jump/left/1.png")
addSpriteImage(playerJumpLeft,"sprite sheets/player/jump/left/2.png")
addSpriteImage(playerJumpLeft,"sprite sheets/player/jump/left/3.png")
addSpriteImage(playerJumpLeft,"sprite sheets/player/jump/left/4.png")
addSpriteImage(playerJumpLeft,"sprite sheets/player/jump/left/5.png")
#up
playerUp = makeSprite("sprite sheets/player/stand/4.png")
addSpriteImage(playerUp,"sprite sheets/player/run/up/1.png")
addSpriteImage(playerUp,"sprite sheets/player/run/up/2.png")



#aderecosImoveis

#skeleton
alienSkeleton = makeSprite("sprite sheets/station/skeleton.png")
#buraco
buraco = makeSprite("sprite sheets/map/buraco.png")
#rocks
rock1 = makeSprite("sprite sheets/map/rock 1.png")
rock2 = makeSprite("sprite sheets/map/rock 2.png")
rock3 = makeSprite("sprite sheets/map/rock 3.png")
rock4 = makeSprite("sprite sheets/map/rock 4.png")




#aderecosMoveis

#bot
bot = makeSprite("sprite sheets/bot/bot#1.png")
addSpriteImage(bot,"sprite sheets/bot/bot#2.png")
addSpriteImage(bot,"sprite sheets/bot/bot#3.png")
addSpriteImage(bot,"sprite sheets/bot/bot#4.png")
addSpriteImage(bot,"sprite sheets/bot/bot#5.png")
addSpriteImage(bot,"sprite sheets/bot/bot#6.png")
addSpriteImage(bot,"sprite sheets/bot/bot#7.png")

#tree
treeSprite = makeSprite("sprite sheets/alienTree/tree#1.png")
addSpriteImage(treeSprite,"sprite sheets/alienTree/tree#2.png")
addSpriteImage(treeSprite,"sprite sheets/alienTree/tree#3.png")
addSpriteImage(treeSprite,"sprite sheets/alienTree/tree#4.png")
addSpriteImage(treeSprite,"sprite sheets/alienTree/tree#5.png")
addSpriteImage(treeSprite,"sprite sheets/alienTree/tree#6.png")
addSpriteImage(treeSprite,"sprite sheets/alienTree/tree#11.png")
addSpriteImage(treeSprite,"sprite sheets/alienTree/tree#12.png")
addSpriteImage(treeSprite,"sprite sheets/alienTree/tree#13.png")
addSpriteImage(treeSprite,"sprite sheets/alienTree/tree#14.png")
addSpriteImage(treeSprite,"sprite sheets/alienTree/tree#15.png")
addSpriteImage(treeSprite,"sprite sheets/alienTree/tree#16.png")
addSpriteImage(treeSprite,"sprite sheets/alienTree/tree#17.png")
addSpriteImage(treeSprite,"sprite sheets/alienTree/tree#18.png")
addSpriteImage(treeSprite,"sprite sheets/alienTree/tree#19.png")

#tree.2
treeSprite2 = makeSprite("sprite sheets/alienTree/tree#1.png")
addSpriteImage(treeSprite2,"sprite sheets/alienTree/tree#2.png")
addSpriteImage(treeSprite2,"sprite sheets/alienTree/tree#3.png")
addSpriteImage(treeSprite2,"sprite sheets/alienTree/tree#4.png")
addSpriteImage(treeSprite2,"sprite sheets/alienTree/tree#5.png")
addSpriteImage(treeSprite2,"sprite sheets/alienTree/tree#6.png")
addSpriteImage(treeSprite2,"sprite sheets/alienTree/tree#11.png")
addSpriteImage(treeSprite2,"sprite sheets/alienTree/tree#12.png")
addSpriteImage(treeSprite2,"sprite sheets/alienTree/tree#13.png")
addSpriteImage(treeSprite2,"sprite sheets/alienTree/tree#14.png")
addSpriteImage(treeSprite2,"sprite sheets/alienTree/tree#15.png")
addSpriteImage(treeSprite2,"sprite sheets/alienTree/tree#16.png")
addSpriteImage(treeSprite2,"sprite sheets/alienTree/tree#17.png")
addSpriteImage(treeSprite2,"sprite sheets/alienTree/tree#18.png")
addSpriteImage(treeSprite2,"sprite sheets/alienTree/tree#19.png")

#tree.3
treeSprite3 = makeSprite("sprite sheets/alienTree/tree#1.png")
addSpriteImage(treeSprite3,"sprite sheets/alienTree/tree#2.png")
addSpriteImage(treeSprite3,"sprite sheets/alienTree/tree#3.png")
addSpriteImage(treeSprite3,"sprite sheets/alienTree/tree#4.png")
addSpriteImage(treeSprite3,"sprite sheets/alienTree/tree#5.png")
addSpriteImage(treeSprite3,"sprite sheets/alienTree/tree#6.png")
addSpriteImage(treeSprite3,"sprite sheets/alienTree/tree#11.png")
addSpriteImage(treeSprite3,"sprite sheets/alienTree/tree#12.png")
addSpriteImage(treeSprite3,"sprite sheets/alienTree/tree#13.png")
addSpriteImage(treeSprite3,"sprite sheets/alienTree/tree#14.png")
addSpriteImage(treeSprite3,"sprite sheets/alienTree/tree#15.png")
addSpriteImage(treeSprite3,"sprite sheets/alienTree/tree#16.png")
addSpriteImage(treeSprite3,"sprite sheets/alienTree/tree#17.png")
addSpriteImage(treeSprite3,"sprite sheets/alienTree/tree#18.png")
addSpriteImage(treeSprite3,"sprite sheets/alienTree/tree#19.png")

#texts
alienhead = makeTextBox(250,550,360,10,"Theres some strange mysteries over here!",100,22)
bottalk = makeTextBox(250,550,360,10,"Carefull where you going!",100,22)
playertalk=makeTextBox(250,550,360,10,"Whats that!",100,22)
leave = makeTextBox(700,20,60,1,"E - leave",50,15)
warning = makeTextBox(250,550,360,10,"Warning! Dangerous area!",100,22)
wild = makeTextBox(250,550,360,10,"That's wild! Not going any closer than this!",100,22)



