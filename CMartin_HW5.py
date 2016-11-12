#This is a small exploration into Data Mining.
#We'll use this example in the future when we look at the more sophisticated mathematical and graphics tools in Python.  

#Do the following:

#Part 1
#Download the new data set on the Lesson 5 page called brainandbody.csv.
#This file is a small set of average brain weights and average body weights for a number of animals.
#We want to see if a relationship exists between the two. (This data set acquired above).

import pandas as pd

url = 'https://raw.githubusercontent.com/chrisgmartin/DATA602/master/brainandbody.csv'
c = pd.read_csv(url)

#Part 2
#Perform a linear regression using the least squares method on the relationship of brain weight [br] to body weight [bo].
#Do this using just the built in Python functions (this is really easy using scipy, but we're not there yet).
#We are looking for a model in the form bo = X * br + Y.
#Find values for X and Y and print out the entire model to the console. 

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