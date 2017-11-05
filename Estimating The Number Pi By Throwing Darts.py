
####ESTIMATING PI WITH DARTS####

import random
from math import pi
import matplotlib.pyplot as plt


def throwdarts(n):
    circle, square, pi_estimation = 0,0,0
    pi_estimations,differences,differences_proportions, confidences = [],[],[], []

    #throw darts#
    for i in range(0,n):            #running n experiments
        x = random.random()
        y = random.random()
        if (x**2 + y**2) <= 1 :     #checking if my dart fell inside(or on) the circle
                   circle += 1      #if so , incrementing to the circle darts counter
        square += 1                 #incrementing the square counter

        pi_estimation = 4.0*circle/square
        #difference = pi_estimation - pi
        pi_estimations.append(pi_estimation)

        #calculating error as 95% confidence interval for error bar:
        #As this is binomial probability (inside or outside the circle),
        #I use binomial distribution SE: sqrt(p(1-p)/n)
        #probability for landing inside the circle is: estimated pi / 4
        p = pi_estimation/4.0
        se = (p*(1.0-p)/float(n))**0.5
        confidence = 1.96*se
        confidences.append(confidence)
    print "Estimation of pi: ", pi_estimation


    ###graphing pi estimations with differences###
    plt.figure()
    plt.title('Pi Estimation for each N darts thrown')
    plt.xlabel("darts")
    plt.ylabel("Pi estimation")
    #plotting estimationm and difference as proportion from pi
    plt.errorbar(range(n),pi_estimations, yerr=confidences, capsize=3, fmt='-o', color='red', label='estimated pi')
    #plotting real value of pi, and 0 to compare)
    plt.plot(range(n),[pi for _ in range(n)], color='green', label='real Pi')
    plt.plot(range(n),[0 for _ in range(n)], color='black')
    plt.legend(fancybox=True)
    plt.show()

    return pi_estimation

print throwdarts(10000)
