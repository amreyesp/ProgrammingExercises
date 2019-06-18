# ProgrammingExercises
A repository with the resolution of some stereotypical programming exercises for developers

## Typical
**FizzBuzz Test:** is an interview question designed to help filter out the 99.5% of programming job candidates who can't seem to program their way out of a wet paper bag. The text of the programming assignment is as follows:
"Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”."

**Program for Conway’s Game Of Life:** Initially, there is a grid with some cells which may be alive or dead. Our task to generate the next generation of cells based on the following rules:
1. Any live cell with fewer than two live neighbors dies, as if caused by under population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

## Warmup
**Sock Merchant:** John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are. For example, there are 7 socks with ar=[1,2,1,2,1,3,2] colors . There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.

**Jumping on the Clouds:** Emma is playing a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2. She must avoid the thunderheads. Determine the minimum number of jumps it will take Emma to jump from her starting position to the last cloud. It is always possible to win the game.

For each game, Emma will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided. For example,  c=[0,1,0,0,0,1,0] indexed from [0...6]. The number on each cloud is its index in the list so she must avoid the clouds at indexes 1 and 5. She could follow the following two paths: 0->2->4->6 or 0->2->3->4->6. The first path takes 3 jumps while the second takes 4.

**Repeated String:** Lilah has a string, s, of lowercase English letters that she repeated infinitely many times. Given an integer, n, find and print the number of letter a's in the first n letters of Lilah's infinite string.
For example, if the string s='abcac' and n=10, the substring we consider is abcacabcac, the first 10 characters of her infinite string. There are 4 occurrences of a in the substring.

## Arrays
**Left Rotation:** A left rotation operation on an array shifts each of the array's elements 1 unit to the left. For example, if 2 left rotations are performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2].
Given an array a of n integers and a number, d, perform d left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.

**New year chaos:** It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! There are a number of people queued up, and each person wears a sticker indicating their initial position in the queue. Initial positions increment by 1 from 1 at the front of the line to n at the back.
Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap positions, they still wear the same sticker denoting their original places in line. One person can bribe at most two others. For example, if n=8 and Person 5 bribes Person 4, the queue will look like this: 1,2,3,5,4,6,7,8.
Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get the queue into its current state!
Print an integer denoting the minimum number of bribes needed to get the queue into its final state. Print Too chaotic if the state is invalid, i.e. it requires a person to have bribed more than 2 people.
