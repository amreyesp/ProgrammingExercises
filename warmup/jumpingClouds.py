"""Jumping on the clouds"""

"""
Emma is playing a new mobile game that starts with consecutively numbered clouds.
Some of the clouds are thunderheads and others are cumulus. She can jump on any
cumulus cloud having a number that is equal to the number of the current cloud
plus 1 or 2. She must avoid the thunderheads. Determine the minimum number of
jumps it will take Emma to jump from her starting position to the last cloud. It
is always possible to win the game.

For each game, Emma will get an array of clouds numbered 0 if they are safe or 1
if they must be avoided. For example,  c=[0,1,0,0,0,1,0] indexed from [0...6].
The number on each cloud is its index in the list so she must avoid the clouds
at indexes 1 and 5. She could follow the following two paths: 0->2->4->6 or
0->2->3->4->6. The first path takes 3 jumps while the second takes 4.
Credits: www.hackerrank.com
"""
import random

class Game:

    def __init__(self):
        self.clouds = []
        self.path = []
        self.steps = 0

    def clouding(self,size):
        for cloud in range(size):
            self.clouds.append(random.randint(0,1))

    def adjustClouding(self):
        self.clouds[0] = 0 #can't initialize on thunderhead (e.g. 1)
        self.clouds[len(self.clouds)-1] = 0 #can't finish on thunderhead
        for i in range(len(self.clouds)-2):
            if self.clouds[i+1] == 1 and self.clouds[i+2] == 1:
                self.clouds[i+2] = 0

    def jumpBack(self,currentCloud):
        if currentCloud>1 and self.clouds[currentCloud-2] == 0:
            targetCloud = currentCloud-2
        else:
            targetCloud = currentCloud-1
        return targetCloud

    def jumpAhead(self,currentCloud):
        if currentCloud<len(self.clouds)-2 and self.clouds[currentCloud+2] == 0:
            targetCloud = currentCloud+2
        else:
            targetCloud = currentCloud+1
        return targetCloud

    def searchPath(self,mode,initialPosition):
        currentCloud = initialPosition
        pathEnd = False

        if mode == 'ahead':
            while pathEnd == False:
                if currentCloud >= len(self.clouds)-3:
                    pathEnd = True
                targetCloud = self.jumpAhead(currentCloud)
                self.path.append(targetCloud)
                currentCloud = targetCloud

        if mode == 'backward':
            while pathEnd == False:
                targetCloud = self.jumpBack(currentCloud)
                self.path.append(targetCloud)
                currentCloud = targetCloud
                if currentCloud == 0:
                    pathEnd = True

    def countSteps(self):
        self.steps = len(self.path)
