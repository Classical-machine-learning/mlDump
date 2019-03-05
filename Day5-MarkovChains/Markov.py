'''
When Cj is sad, which isn't very usual: she either goes for a run, goobles down icecream or takes a nap.

From historic data, if she spent sleeping a sad day away. The next day it is 60% likely she will go for a run, 20% she will stay in bed the next day and 20% chance she will pig out on icecream.

When she is sad and goes for a run, there is a 60% chances she'll go for a run the next day, 30% she gorges on icecream and only 10% chances she'll spend sleeping the next day.

Finally, when she indulges on icecream on a sad day, there is a mere 10% chance she continues to have icecream the next day as well, 70% she is likely to go for a run and 20% chance that she spends sleeping the next day.
'''

## The above is made into a cyclic graph/transition matrix

import numpy as np
import random as rm
states = ['Sleep','Icecream','Run']
transitionName = [["SS","SR","SI"],["RS","RR","RI"],["IS","IR","II"]]
transitionMatrix = [[0.2,0.6,0.2],[0.1,0.6,0.3],[0.2,0.7,0.1]]

if sum(transitionMatrix[0])+sum(transitionMatrix[1])+sum(transitionMatrix[1]) != 3:
    print("Check your probabilities")
    exit(0)

def execute_list(l):
    for a in l:
        a

def activity_forecast(days):
    activityToday = 'Run'
    activityList = [activityToday]
    i,prob = 0,1
    while i != days:
        if activityToday == "Sleep":
            change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
            if change == "SS":
                prob = prob * 0.2
                activityList.append("Sleep")
                pass
            elif change == "SR":
                prob = prob * 0.6
                activityToday = "Run"
                activityList.append("Run")
            else:
                prob = prob * 0.2
                activityToday = "Icecream"
                activityList.append("Icecream")
        elif activityToday == "Run":
            change = np.random.choice(transitionName[1],replace=True,p=transitionMatrix[1])
            if change == "RR":
                prob = prob * 0.5
                activityList.append("Run")
                pass
            elif change == "RS":
                prob = prob * 0.2
                activityToday = "Sleep"
                activityList.append("Sleep")
            else:
                prob = prob * 0.3
                activityToday = "Icecream"
                activityList.append("Icecream")
        elif activityToday == "Icecream":
            change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
            if change == "II":
                prob = prob * 0.1
                activityList.append("Icecream")
                pass
            elif change == "IS":
                prob = prob * 0.2
                activityToday = "Sleep"
                activityList.append("Sleep")
            else:
                prob = prob * 0.7
                activityToday = "Run"
                activityList.append("Run")
        i += 1    
    return activityList

list_activity = []
count = 0

for a in range(1,1000):
    list_activity.append(activity_forecast(2))

for ls in list_activity:
    if(ls[2]=='Run'):
        count+=1


perc = (count/1000)*100
print("prob of starting at Run and ending at RUn is "+str(perc))
