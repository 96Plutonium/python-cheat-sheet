#!/usr/bin/python3.6
#python cheat-sheet

#def-function and lambda-function
#use lambda functions for one-lined code like
#def-example
def sum(x,y):
	return x + y
print(sum(2,2))
#lambda example
sum = lambda x,y: x + y
print(sum(2,2))
#N.B you dont have to write return keyword in lambda-functions

#one-lined for loops
#yup, python can be one lined
for _ in "HELLOWORLD": print(_)
#N.B for works only with iterable-objects
#map() function
#map is better for one lined loops
#example:
squares = map(lambda x: x * x, [0, 1, 2, 3, 4])
for _ in squares: print(_)
#syntax: map(func, list)

#decorators
#@-char is syntax-sugar for decorators
#you can run function that runes another function
#example:
def decorator(func):
	print("IM DECORATOR")
	return func
@decorator
def helloworld():
	print("helloworld")
helloworld()
#you can write log-decorators for example
#you can combine some more decorators to one functions!
def decorator_two(func):
	print("IM DECORATOR NUMBER TWO!")
	return func
#now lets rewrite helloworld()
@decorator
@decorator_two
def helloworld():
	print("Helloworld")
helloworld()
#have you seen it?
#decorator number two had been executed before decorator()!
#decorators are executed down-up. Remember this!

#*args and **kwargs
#definetly words args and kwargs doesnt mean anything,
#buf symbols * and ** in function definitions do magic
#with the arguments
#for example
def sum(*args):
	ret = 0
	for _ in args:
		ret += _
	return ret
print(sum(1,2,3,4))
#also there are **
#thats dict() and you can work with ** as with usual dict

#list-generators
#there are easy way to generate list() 
#example
from random import randint
print([randint(0,9) for _ in range(10)])
#there is another surprise with for loop
#here syntax looks like [<action> for _ in <iterable>]

#itertools module
#this module gives more freedom to functional programmers
#there are some things that you can do in pure python
#like infinite progression
from itertools import *
for i in islice(count(10), 5):
    print(i)
#count(start=,step=) is infinite progression
#islice(count, stop) when count == stop function stops
for _ in permutations(["i", 'fuck', 'you']): print(_)
#permutation functions also has r argument
#thats the max lenght
#iterrtools includes great variety of great functions
#that you should know
