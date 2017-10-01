import math

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
                root = None
                break
            x_m = self.midpoint()
            print ('Bisection> Midpoint: ',x_m)

            trivial_x = self.trivial_root()
            print('Bisection> Trivial_x: ',trivial_x)
            if(trivial_x == 0 and type(trivial_x)!=type(False)):
                print('Bisection> Found trivial root')
                root = trivial_x
                break

            if(f(x_p[0])*f(x_m) < 0):
                #x_right = x_middle
                x_p[1] = x_m
            elif(f(x_p[1])*f(x_m) < 0):
                #x_left = x_middle
                x_p[0] = x_m

            accuracy = abs(f(x_m))
            print('Bisection> Accuracy: ',accuracy,'\n')

            if(accuracy<=tolerance):
                root = x_m
                break
            count+=1
        return root
#----------------------Usage
def f(x):
    return (math.cos(x) - x)
interval = [-1,1]
tolerance = 1e-12
maximum_iterations = 10000
#--Solve
solver = BisectionMethod(f,interval,tolerance,maximum_iterations)

print('Found root: ',solver.find_root())