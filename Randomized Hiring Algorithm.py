"""Hire-Assistant: You need to hire a new assistant.
Every day an agency sends a new assistant for you to interview.
If the assistant is better than your current assistant then you hire them.
(Assistant quality is uniformly distributed between 0 and 1.)
Write python code to simulate this.
>>What is the probability that exactly one assistant will be hired?
>>What is the probability that exactly two assistants will be hired?
Plot a graph showing the average number of assistants hired on the y axis,
against the total number of applicants seen on the x axis.
Include both the theoretical estimate and an empirical estimate.
"""
import random
import matplotlib.pyplot as plt
from numpy import mean

probablity_1 = 0
probablity_2 = 0
probablity_other = 0
hireds = []

def hire_assistant(n):
    global probablity_1, probablity_2, probablity_other, hired
    existing_assist_quality = 0
    #print "existing_assist_quality:", existing_assist_quality
    hired = 0
    for a in xrange(n):
        current_quality = random.random()
        #print "current_quality: ", current_quality
        if current_quality > existing_assist_quality:
            existing_assist_quality = current_quality
            hired += 1
            #print "hired!", hired
    if hired == 1:
        probablity_1 += 1
    if hired == 2:
        probablity_2 += 1
    else:
        probablity_other += 1
    hireds.append(hired)
    return n, existing_assist_quality, hired

def hiring(n, experiments):
    global probablity_1, probablity_2, probablity_other, hireds
    for exp in xrange(experiments):
        hire_assistant(n)
    prob_of_exactly_1 = float(probablity_1)/(experiments*n)
    prob_of_exactly_2 = float(probablity_2)/(experiments*n)
    avg_hired = mean(hired)
    #print "interviewd assistants: ", n
    #print "#hired in each exp: ", hireds
    #print "avg hired: ", hired
    #print "#hiring procedures experiments:", experiments
    #print "prob_of_exactly_1: %.5f"  % float(prob_of_exactly_1)
    #print "prob_of_exactly_2: %.5f" % float(prob_of_exactly_2)
    return avg_hired

def plot_hiring(experiments):
    avgs_hired = []
    for n in range(1,1000):
        avgs_hired.append(hiring(n, experiments))
    plt.plot(range(1,1000),avgs_hired)
    plt.title("Average Number of Hires for each N interviews")
    plt.grid(10)
    plt.show()

#print hiring(10,10)
plot_hiring(100)