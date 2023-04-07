# Daily Coding Interview Problems.
This repository contains [daily coding problem](https://www.dailycodingproblem.com/) solution implemented in python.

## Problems
### [Problem 010323](solutions/dcp_01_03.py)

The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N. 
The method is to take increasingly larger prime numbers, and mark their multiples as composite.

For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two), 
then [6, 9, 12, ...] (multiples of three), and so on. Once we have done this for all primes less than N, 
the unmarked numbers that remain will be prime.

Implement this algorithm.

Bonus: Create a generator that produces primes indefinitely (that is, without taking N as an input).

---
### [Problem 020323](solutions/dcp_02_03.py)

You are given an array of integers, where each element represents the maximum number of steps that can be jumped going forward from that element. Write a function to return the minimum number of jumps you must take in order to get from the start to the end of the array.

For example, given [6, 2, 4, 0, 5, 1, 1, 4, 2, 9], you should return 2, as the optimal solution involves jumping from 6 to 5, and then from 5 to 9.

---
### [Problem 030323](solutions/dcp_03_03.py)

Given a list of words, determine whether the words can be chained to form a circle. 
A word X can be placed in front of another word Y in a circle if the last character of X is same as the first character of Y.

For example, the words ['chair', 'height', 'racket', touch', 'tunic'] 
can form the following circle: chair --> racket --> touch --> height --> tunic --> chair

---
### [Problem 040323](solutions/dcp_04_03.py)

Given a binary tree, determine whether or not it is height-balanced. A height-balanced binary tree can 
be defined as one in which the heights of the two subtrees of any node never differ by more than one.

Example:

Input: root = [1,2,2,3,3,null,null,4,4]

Output: false


---
### [Problem 050323](solutions/dcp_05_03.py)

Find the maximum of two numbers without using any if-else statements, branching, or direct comparisons.

Example:

Inputs: x = 3, y = 4

Output: 4


---

