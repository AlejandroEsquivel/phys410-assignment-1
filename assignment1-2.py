#!/usr/bin/python

# Assignment 1 - Question 2
# Author: Alejandro Esquivel, Student#: 28489145
# Enviroment: Mac OS-X Sierra, Python 3.5.2
# assumptions: numpy is installed globally or in virtual env using pip.

import math
import numpy as np

class NewtonsMethodMultivariate:
    def __init__(self, f1, f2, df1_dx, df2_dx,df1_dy, df2_dy, r,tolerance,maximum_iterations):
      self._f1 = f1
      self._f2 = f2
      self._df1_dx = df1_dx
      self._df2_dx = df2_dx
      self._df1_dy = df1_dy
      self._df2_dy = df2_dy
      self.r = r
      self._maximum_iterations = maximum_iterations
      self._tolerance = tolerance;


    def f(self,x,y):
        f1 = self._f1 
        f2 = self._f2
        return [f1(x,y),f2(x,y)];
    
    def jacobian(self,x,y):
        df1_dx = self._df1_dx
        df2_dx = self._df2_dx
        df1_dy = self._df1_dy
        df2_dy = self._df2_dy
        return np.matrix([[df1_dx(x,y),df1_dy(x,y)],[df2_dx(x,y),df2_dy(x,y)]]);

    def jacobian_inv(self,x,y):
        return np.linalg.inv(jacobian(x,y));

    def norm(self,r):
        return math.sqrt(np.dot(r,r))

    def iterate(self,x,y):
        M = np.dot(self.jacobian_inv(x,y),self.f(x,y))
        r_new = np.array(np.subtract([x,y],M)).flatten()
        #rint('r_new: ',r_new);
        #print('input: ',[x,y]);
        #print('f1: ',f1(r_new[0],r_new[1]))
        #print('f2: ',f2(r_new[0],r_new[1]))
        #print('norm_of_f: ',self.norm(self.f(r_new[0],r_new[1])))
        #print('\n')
        return r_new;

    def find_root(self): 
        maximum_iterations = self._maximum_iterations
        tolerance = self._tolerance 

        i = 0
        accuracy = 100*tolerance
        while(True):
            i+=1
            self.r = self.iterate(self.r[0],self.r[1]);
            if(self.norm(self.f(self.r[0],self.r[1])) < tolerance):
                root = self.r
                break;
            if(i>maximum_iterations):
                root = None;
                break;
            #accuracy = 
            #print('new r');
            #print(self.r);
            #print('\n')
        return root;




def f1(x,y):
    return x**2 - 2*x - y + 0.5

def f2(x,y):
    return x**2 + 4*(y**2) - 4.0

def df1_dx(x,y):
    return 2*x - 2

def df2_dx(x,y):
    return 2*x

def df1_dy(x,y):
    return -1

def df2_dy(x,y):
    return 8*y

def jacobian(x,y):
    return np.matrix([[df1_dx(x,y),df1_dy(x,y)],[df2_dx(x,y),df2_dy(x,y)]]);


def f(x,y):
    return [f1(x,y),f2(x,y)]



r = [0.01,0.01]

maximum_iterations = 1000
tolerance = 1e-12

root = NewtonsMethodMultivariate(f1,f2,df1_dx,df2_dx,df1_dy,df2_dy,r,tolerance,maximum_iterations).find_root()

if(type(root)!=type(None)):
    print('\n\nFound root: ',root,'\n')
else:
    print('\n\nDid not find root within ',maximum_iterations,'\n')




