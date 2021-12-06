import noise
import numpy as np

#octaves aantal detail je wilt
#persistence soort van amplitude
#lacunarity hoeveel detail je per octaves wilt of niet
class Generate():
    #Wereled kleur
    lightblue = [0,191,255]
    blue = [65,105,225]
    green = [34,139,34]
    darkgreen = [0,100,0]
    sandy = [210,180,140]
    beach = [238, 214, 175]
    snow = [255, 250, 250]
    mountain = [139, 137, 137]
    #Terein bereik
    seaLevel = -0.05
    beacheLvel = 0
    sandLevel = 0.08
    greenLevel = 0.2
    darkGreenLevel = 0.35
    mountenLevel = 0.4
    
    def __init__(self,width=1024,height=1024,octaves=6,persistence=0.5,lacunarity=2.0,scale=100,seed=100):
        self.width =width
        self.height =height
        self.octaves = octaves
        self.persistence = persistence
        self.lacunarity = lacunarity
        self.scale = scale
        self.seed = seed
        self.shape = (self.width,self.height)
        self.world = np.zeros(self.shape)
    
    def maakNoise(self):
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                self.world[i][j] = noise.pnoise2(i/self.scale, 
                                    j/self.scale, 
                                    octaves=self.octaves, 
                                    persistence=self.persistence, 
                                    lacunarity=self.lacunarity, 
                                    repeatx=self.width, 
                                    repeaty=self.height, 
                                    base=self.seed)
    
    def maakWereld(self):
        self.maakNoise()
        color_world = np.zeros(self.world.shape+(3,))
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                if self.world[i][j] < self.seaLevel:
                    color_world[i][j] = self.blue
                elif self.world[i][j] < self.beacheLvel:
                    color_world[i][j] = self.beach
                elif self.world[i][j] < self.sandLevel:
                    color_world[i][j] = self.sandy
                elif self.world[i][j] < self.greenLevel:
                    color_world[i][j] = self.green
                elif self.world[i][j] < self.darkGreenLevel:
                    color_world[i][j] = self.darkgreen
                elif self.world[i][j] < self.mountenLevel:
                    color_world[i][j] = self.mountain
                else:
                    color_world[i][j] = self.snow

        return color_world


class Eiland(Generate):
    #Terein bereik
    seaLevel = 0.1
    beacheLvel = 0.25
    sandLevel = 0.26
    greenLevel = 0.35
    darkGreenLevel = 0.50
    mountenLevel = 0.60


class Landschap(Generate):
    flower = [218,112,214]
    #Terein bereik
    greenLevel = -0.02
    flowerLevel = 0.01
    darkGreenLevel = 0.2
    mountenLevel = 0.5
    
    
    def maakWereld(self):
        self.maakNoise()
        color_world = np.zeros(self.world.shape+(3,))
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                if self.world[i][j] < self.greenLevel:
                    color_world[i][j] = self.green
                elif self.world[i][j] < self.flowerLevel:
                    color_world[i][j] = self.flower
                elif self.world[i][j] < self.darkGreenLevel:
                    color_world[i][j] = self.darkgreen
                elif self.world[i][j] < self.mountenLevel:
                    color_world[i][j] = self.mountain
                else:
                    color_world[i][j] = self.snow

        return color_world

class Mounten(Generate):
    #Wereled kleur
    green = [34,139,34]
    darkgreen = [0,100,0]
    mountain = [139, 137, 137]
    monuIce = [78,108,180]
    
    #Terein bereik
    greenLevel = -0.9
    darkGreenLevel = -0.1
    mountenLevel = 0.09
    monuIceLevel = 0.22
    
    
    
    def maakWereld(self):
        self.maakNoise()
        color_world = np.zeros(self.world.shape+(3,))
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                if self.world[i][j] < self.greenLevel:
                    color_world[i][j] = self.green
                elif self.world[i][j] < self.darkGreenLevel:
                    color_world[i][j] = self.darkgreen
                elif self.world[i][j] < self.mountenLevel:
                    color_world[i][j] = self.mountain
                elif self.world[i][j] < self.monuIceLevel:
                    color_world[i][j] = self.monuIce
                else:
                    color_world[i][j] = self.snow

        return color_world
    