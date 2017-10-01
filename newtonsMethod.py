import math

#convention: object variables preffixed with _
#            methods do are not preffixed.
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
            print('Newton> Iteration: ',count)
            print('Newton> x = ',x)
            print('Newton> |f(x)| = ',accuracy,'\n')
            if(accuracy<tolerance):
                root = x
                break
            count+=1
        return root
#----------------------Usage
def f(x):
    return (math.cos(x) - x)
def f_prime(x):
    return (-1*math.sin(x) - 1)

x_o = 1
tolerance = 1e-12
maximum_iterations = 100000

solver = NewtonsMethod(f,f_prime,x_o,tolerance,maximum_iterations)

print('Found root: ',solver.find_root())