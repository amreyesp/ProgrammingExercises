"""New year chaos"""
"""
It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride!
There are a number of people queued up, and each person wears a sticker indicating
their initial position in the queue. Initial positions increment by 1 from 1 at
the front of the line to n at the back.
Any person in the queue can bribe the person directly in front of them to swap
positions. If two people swap positions, they still wear the same sticker denoting
their original places in line. One person can bribe at most two others.
For example, if n=8 and Person 5 bribes Person 4, the queue will look like this:
1,2,3,5,4,6,7,8.
Fascinated by this chaotic queue, you decide you must know the minimum number of
bribes that took place to get the queue into its current state!
Print an integer denoting the minimum number of bribes needed to get the queue
into its final state. Print Too chaotic if the state is invalid, i.e. it
requires a person to have bribed more than 2 people.
Credits: www.hackerrank.com
"""

import random, numpy

class Queue:

    def __init__(self):
        self.size = 0
        self.queue = []
        self.bribes = 0
        self.output = ''

    def initialState(self,size):
        self.size = size
        self.queue = [element+1 for element in range(size)]

    def finalState(self):
        random.shuffle(self.queue)

    def invalidState(self):
        for index,element in numpy.ndenumerate(self.queue):
            if element - (index[0]+1) > 2:
                self.output = 'Too chaotic'
                return True
        return False

    def prevState(self,currentState):
        elementdif = []
        max_bribes = 0
        for index,element in numpy.ndenumerate(currentState):
            dif = element - (index[0]+1)
            elementdif.append(dif)
            if dif >= max_bribes:
                max_bribes = dif
                index1 = index[0]
                index2 = index[0]+max_bribes
        #swap elements
        self.bribes = self.bribes + max_bribes
        element1=currentState[index1]
        currentState.remove(element1)
        currentState.insert(index2,element1)
        return currentState

    def countBribes(self,finalQueue):
        currentState = finalQueue.copy()
        initialQueue = finalQueue.copy()
        initialQueue.sort()
        while currentState != initialQueue:
            currentState = self.prevState(currentState)

def main():
    myQueue = Queue()
    myQueue.initialState(5)
    myQueue.finalState()
    print('Final queue:',myQueue.queue)
    #Check if the final state is invalid
    if myQueue.invalidState():
        print(myQueue.output)
    else:
        myQueue.countBribes(myQueue.queue)
        print('The minimum number of bribes was:',myQueue.bribes)

if __name__== '__main__':
    main()
