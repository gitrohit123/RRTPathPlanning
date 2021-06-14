import random
import math
import pygame

class RRTMap:
    def __init__(self,start,goal,MapDimensions,obsdim,obsnum):
        self.start=start
        self.goal=goal
        self.MapDimensions=MapDimensions
        self.Maph,self.Mapw=self.MapDimensions

        self.MapWindowName='RRT Path Planning'
        pygame.display.set_caption(self.MapWindowName)
        self.map=pygame.display.set_mode((self.Mapw, self.Maph))
        self.map.fill((255, 255, 255))
        self.nodeRad = 0
        self.nodeThickness = 0
        self.edgeThickness = 1

        self.obstacles = []
        self.obsdim = obsdim
        self.obsNumber = obsnum

        self.grey = (70, 70, 70)
        self.Blue = (0, 0, 255)
        self.Green = (0, 255, 0)
        self.Red = (255, 0, 0)
        self.white = (255, 255, 255)


    def drawMap(self):
        pass

    def drawPath(self):
        pass

    def drawObs(self):
        pass

class RRTGraph:
    def __init__(self,start,goal,MapDimensions,obsdim,obsnum):
        (x,y) = start
        self.start = start
        self.goal = goal
        self.goalFlag = False
        self.Maph

    def makeRandomRect(self):
        pass

    def makeobs(self):
        pass

    def add_node(self):
        pass

    def remove_node(self):
        pass

    def add_edge(self):
        pass

    def remove_edge(self):
        pass

    def number_of_nodes(self):
        pass

    def distance(self):
        pass

    def nearest(self):
        pass

    def isFree(self):
        pass

    def crossobstacle(self):
        pass

    def connect(self):
        pass

    def step(self):
        pass

    def path_to_goal(self):
        pass

    def getpathCoords(self):
        pass

    def bias(self):
        pass

    def expand(self):
        pass

    def cost(self):
        pass
