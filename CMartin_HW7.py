#What we are doing here is very similar to homework 6, but now we'll look a bit at scipy.
#Do parts 1 and 2.  Part 3 is optional.

#Part One:
#    Take what you did on homework 5 as a starting point (using any of the provided datasets).
#    Replace the regression calculation using least squares with a curve fitting approach (examples in the reading).
#    To start, just fit a linear equation.  Output the equation to the console.
#    You don't need to graph anything (we'll look at that in a couple more weeks).

import pandas as pd
from scipy.optimize import curve_fit

url = 'https://raw.githubusercontent.com/chrisgmartin/DATA602/master/brainandbody.csv'
c = pd.read_csv(url)
body = c['body']
brain = c['brain']


#ORIGINAL SOLUTION
xavg = sum(c['brain'])/len(c['brain'])
yavg = sum(c['body'])/len(c['body'])
#slope = sum((x-xavg)(y-yavg))/sum((x-xavg)^2)
c['x'] = c['brain']-xavg
c['y'] = c['body']-yavg
c['x2'] = (c['brain']-xavg)*(c['brain']-xavg)
c['xy'] = c['x']*c['y']
slope = sum(c['xy'])/sum(c['x2'])
#intercept = (sum(y)*sum(x^2) - sum(x)*sum(x*y)) / (n*sum(x^2)-sum(x)^2)
intercept = (sum(c['y']) * sum(c['x2']) - sum(c['x']) * sum(c['xy'])) / (len(c['x']) * sum(c['x2']) - sum(c['x'])*sum(c['x']))
print "body size = ", intercept, " * brain size + ", slope

#NEW SOLUTION USING SCIPY
x = c['brain']
y = c['body']
def func(x, a, b):
    return a * x + b
# Executing curve_fit on noisy data
popt, pcov = curve_fit(func, x, y)
# popt returns the best fit values for parameters of
# the given model (func).
print popt

#Part Two:
#    Again, using timeit, compare the performance of your solution in homework 5 to the scipy function.
#    Output the results to the console.

setup = '''
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import copy

url = 'https://raw.githubusercontent.com/chrisgmartin/DATA602/master/brainandbody.csv'
c = pd.read_csv(url)
body = c['body']
brain = c['brain']

#Original Function
def manualregression(input, output):
    xavg = sum(input)/len(input)
    yavg = sum(output)/len(output)
    c['x'] = input-xavg
    c['y'] = output-yavg
    c['x2'] = (input-xavg)*(input-xavg)
    c['xy'] = c['x']*c['y']
    slope = sum(c['xy'])/sum(c['x2'])
    intercept = (sum(c['y']) * sum(c['x2']) - sum(c['x']) * sum(c['xy'])) / (len(c['x']) * sum(c['x2']) - sum(c['x'])*sum(c['x']))
    return "body size = ", intercept, " * brain size + ", slope

#New Function
def scipyregression(input, output):
    x = input
    y = output
    def func(x, a, b):
        return a * x + b
    popt, pcov = curve_fit(func, x, y)
    return  "body size = ", popt[0], " * brain size + ", popt[1]
'''

popt[0]

import timeit
n=100
t_fun1 = timeit.timeit("x=copy.copy(brain); y=copy.copy(body); manualregression(x, y)", setup=setup, number=n)
t_fun2 = timeit.timeit("x=copy.copy(brain); y=copy.copy(body); scipyregression(x, y)", setup=setup, number=n)

n2=1000
t2_fun1 = timeit.timeit("x=copy.copy(brain); y=copy.copy(body); manualregression(x, y)", setup=setup, number=n2)
t2_fun2 = timeit.timeit("x=copy.copy(brain); y=copy.copy(body); scipyregression(x, y)", setup=setup, number=n2)

n3=10000
t3_fun1 = timeit.timeit("x=copy.copy(brain); y=copy.copy(body); manualregression(x, y)", setup=setup, number=n3)
t3_fun2 = timeit.timeit("x=copy.copy(brain); y=copy.copy(body); scipyregression(x, y)", setup=setup, number=n3)

print '''
Function Run         100 Times  1000 Times  10000 Times
------------------------------------------------------------
Original Function:   %.4f sec   %.4f sec   %.4f sec
New Function     :   %.4f sec   %.4f sec   %.4f sec
------------------------------------------------------------
''' %(t_fun1, t2_fun1, t3_fun1, t_fun2, t2_fun2, t3_fun2)


#Part Three: (Optional)
#    There are other models that can be fitted to the data we have.
#    Try to fit other equations, like Gaussian, to the data.  Output the equation to the console.








