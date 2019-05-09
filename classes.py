from main import *
class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = bulletWidth
        self.height = bulletHeight

    def getXY(self):
        return [self.x, self.y]

class Enemy:
    def __init__(self, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.index = 0
        self.explodeIndex = 0
        self.width = 20
        self.height = 20
        self.isDead = False
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
