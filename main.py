import pygame
import random

enemyInQueue = False
#class Weapon:
#    def __init__(s):

class Player:
    def __init__(self):
        self.width = 40
        self.height = 40
        self.enemiesKilled = 0
        self.hp = 10
        self.fullHp = self.hp
        self.xLoc = width / 2 - self.width / 2
        self.yLoc = height - self.height
        
        # movement variables
        self.xMove = 0
        self.yMove = 0
        self.moveSpeed = 5
        self.weapons = []
        self.defaultShip = pygame.image.load('spaceship.png')
        self.points = 0
    def update(self):
         
        blitImage(self.defaultShip, [self.xLoc, self.yLoc])
class Bullet:
    def __init__(self, x, y, bType='default'):
        self.x = x
        self.y = y
        if bType == 'default':
            self.damage = 1
    def getXY(self):
        return [self.x, self.y]

class Enemy:
    def __init__(self, x, y, eType='default'):
        self.x = x
        self.y = y
        self.index = 0
        self.explodeIndex = 0
        self.isDead = False
        self.eType = eType
        if eType == 'default':
            self.hp = random.randint(1,2)
            self.width = 20
            self.height = 20



    def update(self):
        if self.index == len(enemyIdle) - 1:
            self.index = 0
        else:
            self.index += 1
    def getXY(self):
        return [self.x, self.y]
    def getIndex(self):
        return self.index
    def explode(self):
        if self.isDead == True and self.explodeIndex < len(enemyExplosion):
            
            blitImage(enemyExplosion[enemy.explodeIndex], (self.x - self.width,
            self.y - self.height))
            self.explodeIndex += 1
        else:
            self.explodeIndex = 0
def spawnEnemies(numEnemies):
    for x in range(1, numEnemies):
        enemies.append
    
def update():
    pygame.display.flip()
    
def rectangle(surface,color,location):
    pygame.draw.rect(surface, color, location)

def shoot():
    newBullet = Bullet(player.xLoc + player.width / 2 - bulletWidth / 2, player.yLoc)
    bullets.append(newBullet)
def displayBullets():
    for bullet in bullets:
        bullet.y = bullet.y - 5
        rectangle(screen, (255,255,255), (bullet.x,bullet.y,bulletWidth,bulletHeight))
        if bullet.y < 0:
            del bullet
def limitEnemy(enemy_limit, currentEnemies):
    if len(currentEnemies) >= enemy_limit:
        return True
    else:
        return False
def limitBullets():
    pass
def isCollision(srcXY, tgtXY, sW, sH, tgtW, tgtH):
    sX2 = srcXY[0] + sW
    sY2 = srcXY[1] + sH
    tgtX2 = tgtXY[0] + tgtW
    tgtY2 = tgtXY[1] + tgtH

    if tgtXY[0] > sX2 or tgtX2 < srcXY[0] or tgtXY[1] > sY2 or tgtY2 < srcXY[1]:
        return False
    # has collided
    else:
        return True
def text(surface, font, size, text, color, xy):
    myFont = pygame.font.SysFont(font, size)

    textSurface = myFont.render(text, False, color)

    surface.blit(textSurface, xy)

def load(image):
    pygame.image.load(image)

def blitImage(image, xy):
    screen.blit(image, xy)
def displayHp():
    full = player.fullHp
    hp = player.hp
    
    # red bar
    rectangle(screen, (255, 0, 0), (10, height + hudHeight - (hudHeight / 2), player.fullHp * 10, 20))
    if hp > 0:
        # green bar
        rectangle(screen, (0, 255, 0), (10, height + hudHeight - (hudHeight / 2), player.hp *10, 20))
    
    # put HP text
    text(screen, 'impact', 20, f'{player.hp * 10}%', (0,0,0), (45, height + hudHeight - (hudHeight / 2 + 2)))
#def displayHealth():
#    rectangle([])
# initiate pygame
pygame.init()
pygame.font.init()

# HUD
hudHeight = 100


width, height = 400, 700 - hudHeight
screen = pygame.display.set_mode((width,height + hudHeight)) 
pygame.display.set_caption('Shooter Game')

# colors list
black = (0,0,0) # no color
white = (255,255,255) # all the color

# create clock object
clock = pygame.time.Clock()

# set starting background color
backgroundColor = black

# game variables
gameRound = 1
gameState = 'play'



# make multiplyer for enemies
enemiesToSpawn = gameRound * random.randint(1,3)
# player stuff
player = Player()
#player.width, player.height = 40, 40
bulletWidth, bulletHeight = 5, 5

frame = 0
enemySpeed = 5

# load player sprite

enemy_img = pygame.image.load('enemy.png')

enemyIdle = [pygame.image.load('sprite_00.png'), pygame.image.load('sprite_01.png'),
 pygame.image.load('sprite_02.png'), pygame.image.load('sprite_03.png'), pygame.image.load('sprite_04.png'),
pygame.image.load('sprite_05.png'), pygame.image.load('sprite_06.png'), pygame.image.load('sprite_07.png'), 
pygame.image.load('sprite_08.png'), pygame.image.load('sprite_09.png')]

enemyExplosion = [pygame.image.load('explosion00.png'), pygame.image.load('explosion01.png'), pygame.image.load('explosion02.png'),
pygame.image.load('explosion03.png'), pygame.image.load('explosion04.png'), pygame.image.load('explosion05.png'), 
pygame.image.load('explosion06.png'), pygame.image.load('explosion07.png'), pygame.image.load('explosion08.png'),
 pygame.image.load('explosion09.png')]

# indexes for animation


# enemy stuff
enemies = []
bullets = []
place_enemy = 0
enemyLimit = 1000000
enemyHeight = 20
enemyWidth = 20
enemyFrequency = 100
screenStart = 500


while True:
    
    frame += 1

    # round complete
    if gameState == 'round_complete':
        gameRound += 1
        enemiesToSpawn = gameRound * random.randint(1,3)
        gameState = 'play'
        
        while True:
            exit = False
            # fill background
            screen.fill((0,0,0))

            # delete bullets
            bullets = []

            # make x and y move 0
            player.xMove, player.yMove = 0, 0
            text(screen, 'impact', 20, f'Round {gameRound}...SPACE TO CONTINUE', white, [20, (height + hudHeight) / 2])
            update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        exit = True
                        break
            if exit:
                break
    # keyboard handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # game exit
            pygame.quit()
 
        # if a key is pressed
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:
                player.yMove = -player.moveSpeed
            elif event.key == pygame.K_DOWN:
                player.yMove = player.moveSpeed
            elif event.key == pygame.K_LEFT:
                player.xMove = -player.moveSpeed
            elif event.key == pygame.K_RIGHT:
                player.xMove = player.moveSpeed
            elif event.key == pygame.K_SPACE:
                #if canShoot() == True:

                shoot()
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and player.xMove > 0:
                player.xMove = 0
            if event.key == pygame.K_LEFT and player.xMove < 0:
                player.xMove = 0
            elif event.key == pygame.K_UP and player.yMove < 0:
                player.yMove = 0 
            if event.key == pygame.K_DOWN:
                player.yMove = 0

    # top boundary
    if player.yLoc - player.moveSpeed < 0 and player.yMove < 0:
        player.yMove = 0
    # bottom boundary
    if player.yLoc + player.moveSpeed > height - player.height and player.yMove > 0:
        player.yMove = 0
    if player.xLoc - player.moveSpeed < 0 and player.xMove < 0:
        player.xMove = 0
    if player.xLoc + player.moveSpeed > width - player.width and player.xMove > 0:
        player.xMove = 0
    player.xLoc += player.xMove
    player.yLoc += player.yMove       
    # fill screen with color
    screen.fill(backgroundColor)
    
    
    # enemy spawner
    if limitEnemy(enemyLimit, enemies) == False:
        if enemiesToSpawn > 0:    
            if enemyInQueue == False:
                place_enemy = enemyFrequency + frame
                enemyInQueue = True

            elif frame == place_enemy:
                x = random.randint(0,width - enemyWidth)
                # increment enemy ID
                #enemyId += 1
                # create new enemy
                newEnemy = Enemy(x, -enemyHeight)
                # append new enemy to enemies list
                enemies.append(newEnemy)    
                # There is now no enemy in queue
                enemyInQueue = False
                place_enemy = 0

                # decrement num of enemies to spawn
                enemiesToSpawn -= 1

    # draw ground
    rectangle(screen, (255, 255, 255), (0, height, width, 10))

    # print out enemies
    for enemy in enemies:
        # current enemies position in array if need to delete
        enemyIndex = enemies.index(enemy)

        # check if out of bounds
        if enemy.y > height - enemy.height:
            enemy.isDead = True

        # check if enemy colliding with player
        if isCollision(enemy.getXY(), [player.xLoc, player.yLoc], enemy.width,
         enemy.height, player.width, player.height):
            
            del enemies[enemyIndex]

            if player.hp >0:
                player.hp -= 1

        # enemy is not dead
        if enemy.isDead == False:
            enemy.y += enemySpeed
            blitImage(enemyIdle[enemy.index], [enemy.x, enemy.y])

            # update the index for idle animation
            enemy.update() 

        # enemy is dead  
        else:
            enemy.explode()
        # check if bullet collision for enemy and bullet
        # only check for collision if there is a bullet
        if len(bullets) > 0:   
             
            for bullet in bullets:
                # get bullet index
                bulletIndex = bullets.index(bullet)

                # bullet is colliding with enemy
                if isCollision(enemy.getXY(), bullet.getXY(), enemy.width, enemy.height, bulletWidth, bulletHeight):
                    # take away hp
                    enemy.hp -= bullet.damage
                    if enemy.isDead == False:

                        del bullets[bulletIndex]  
                    # enemy hp is zero or below
                    if enemy.hp <= 0:
                        enemy.isDead = True

        # explosion animation finished
        if enemy.explodeIndex == len(enemyExplosion) - 1:
            # delete enemy
            del enemies[enemyIndex]
        
        # updates the enemy index 
        
    displayBullets()
    displayHp()

    
    # draw character
    player.update()
    #screen.blit(spaceship, player.xLoc, player.player.yLoc)
    
    # check if enemies are dead
    if len(enemies) <= 0 and enemiesToSpawn <= 0:
        gameState = 'round_complete'

    #text(screen, 'impact', 10, f'HP:{player.hp}', white, [0, 0])
    text(screen, 'Comic Sans MS', 10, f'Round:{gameRound}', white, [0, 30])
    text(screen, 'Comic Sans MS', 10, f'NeedToSpawn:{enemiesToSpawn}', white, [0, 60])
    #text(screen, 'Comic Sans MS', 10, f'frame:{frame}', white, [0, 90])
    text(screen, 'Comic Sans MS', 10, f'EnemyFreq:{enemyFrequency}', white, [0, 120])
    # uses flip to update the screen
    update()
    # FPS
    clock.tick(30)
