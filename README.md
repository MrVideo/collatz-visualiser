# Collatz Conjecture Plot Visualiser

A Python script to plot the number sequence generated by a seed through the Collatz conjecture.

## What is the Collatz conjecture?

From [Wikipedia](https://en.wikipedia.org/wiki/Collatz_conjecture):
> The Collatz conjecture is a conjecture in mathematics that concerns sequences defined as follows: start with any positive integer n. Then each term is obtained from the previous term as follows: if the previous term is even, the next term is one half of the previous term. If the previous term is odd, the next term is 3 times the previous term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

## What does this script do?

This script takes a natural number greater or equal than one and follows the rules imposed by the conjecture to then gather an array of integers and plot them with ``matplotlib.pyplot``.

### Known problems

Very big integers converge to 0 instead of 1. I will try to solve this, but it might be caused by approximation errors, which are out of my control.
