#!/usr/bin/python

# Assignment 1 - Question 1
# Author: Alejandro Esquivel, Student#: 28489145
# Enviroment: Mac OS-X Sierra, Python 3.5.2
# assumptions: numpy is installed globally or in virtual env using pip.

import math
import numpy as np

#convention: object variables preffixed with _
#            methods do are not preffixed.
class BisectionMethod:
    def __init__(self, f, interval,tolerance,maximum_iterations):
      self._f = f
      self._interval = interval
      self._tolerance = tolerance
      self._x_p = [interval[0],interval[1]]
      self._maximum_iterations = maximum_iterations
    
    def f(self,x):
        return self._f(x)

    def midpoint(self):
        return (self._x_p[0] + self._x_p[1])/2

    def trivial_root(self):
        x_m = self.midpoint()
        f = self.f
        x_p = self._x_p
        if(f(x_p[0])==0):
            return x_p[0]
        elif(f(x_p[1])==0):
            return x_p[1]
        elif(f(x_m)==0):
            return x_m
        else:
            return False

    def find_root(self):
        x_p = self._x_p
        f = self.f
        tolerance = self._tolerance
        maximum_iterations = self._maximum_iterations

        count = 0
        accuracy = 100*tolerance
        while(True):
            if(count>=maximum_iterations):
                #print('Bisection> no roots for [a,b] = ',interval)
                root = None
                break
            x_m = self.midpoint()
            #print ('Bisection> Midpoint: ',x_m)
            trivial_x = self.trivial_root()
            #print('Bisection> Trivial_x: ',trivial_x)
            if(trivial_x == 0 and type(trivial_x)!=type(False)):
                #print('Bisection> Found trivial root')
                root = trivial_x
                break

            if(f(x_p[0])*f(x_m) < 0):
                #x_right = x_middle
                x_p[1] = x_m
            elif(f(x_p[1])*f(x_m) < 0):
                #x_left = x_middle
                x_p[0] = x_m

            accuracy = abs(f(x_m))
            #print('Bisection> Accuracy: ',accuracy)

            if(accuracy<=tolerance):
                root = x_m
                break
            count+=1
        return root

class NewtonsMethod:

    def __init__(self, f, f_prime, x_o,tolerance,maximum_iterations):
        self._f = f
        self._f_prime = f_prime
        self._x = x_o
        self._tolerance = tolerance
        self._maximum_iterations = maximum_iterations

    def f(self,x):
        return self._f(x)

    def f_prime(self,x):
        return self._f_prime(x)

    def find_root(self):
        tolerance = self._tolerance
        maximum_iterations = self._maximum_iterations
        x = self._x

        accuracy = 1
        count = 0
        while(True):
            if(count>=maximum_iterations):
                print("Newton> Maximum Iterations reached")
                root = None
                break
            if(f_prime(x)==0):
                print("Newton> Prevented division by 0 in f'(",x,")")
                root = None
                break
            x = x - (f(x)/f_prime(x))
            accuracy = abs(f(x))
            #print('Newton> Iteration: ',count)
            #print('Newton> x = ',x)
            #print('Newton> |f(x)| = ',accuracy)
            if(accuracy<tolerance):
                root = x
                break
            count+=1
        return root

def intervalSlice(interval,min_spacing):
    slices = math.ceil((interval[1] - interval[0])/min_spacing)
    spacing = (interval[1]-interval[0])/slices;
    intervals = []
    for i in range(0,slices):
        x_l = (interval[0]+i*spacing)
        x_r = x_l + spacing
        intervals.append([x_l,x_r])
    return intervals

#-------Problem Definition
def f(x):
    return (6425*(x**8) - 12012*(x**6) + 6930*(x**4) - 1260*(x**2) + 35)/128
def f_prime(x):
    return (8*6425*(x**7) - 6*12012*(x**5) + 4*6930*(x**3) - 2*1260*(x) + 35)/128

a_b = [-1,1]
tolerance = 1e-12
maximum_iterations = 100
#--Solve
roots = []
intervals = intervalSlice(a_b,0.01);
for interval in intervals:
    root = BisectionMethod(f,interval,0.001,maximum_iterations).find_root()
    if(type(root) != type(None)):
        root = NewtonsMethod(f,f_prime,root,tolerance,maximum_iterations).find_root()
        if(type(root) != type(None)):
            roots.append(root)

print('\n\nFound roots: ');
print(roots,'\n');

