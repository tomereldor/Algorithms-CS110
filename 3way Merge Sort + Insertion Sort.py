#Merge sort 3way with steps and time:
import time
import random
import matplotlib.pyplot as plt

steps = 0

############## HELPER FUNCTIONS ####################
def merge2(lefthalf,righthalf):
    #print "merge 2: ", lefthalf,righthalf
    global steps #in this function, refer to the glboal "steps" variable
    mergedlst = []
    while len(lefthalf) and len(righthalf) >0:
        steps += 1
        if lefthalf[0] <= righthalf[0]:
            mergedlst.append(lefthalf[0])
            lefthalf.remove(lefthalf[0])
        else:
            mergedlst.append(righthalf[0])
            righthalf.remove(righthalf[0])
        steps += 3
    if len(lefthalf) == 0:
        mergedlst += righthalf
        steps += 1
    if len(righthalf) == 0:
        mergedlst += lefthalf
        steps += 1
    steps += 1
    # # print  "steps = ", steps
    # print  "merged2list = ",mergedlst
    return mergedlst

def merge3(a,b,c):
    # print  "merge 3: ",a,b,c
    global steps
    mergedlst = []
    while len(a) and len(b) and len(c) :
        # print  "legnths: " , len(a), len(b), len(c)
        #steps += 1
        # print  a[0],b[0],c[0]
        if (a[0] <= b[0]) and (a[0] <= c[0]):
            # print  "min = a[0]: ", a[0]
            mergedlst.append(a[0])
            a.remove(a[0])
            steps += 3
        elif (b[0] <= a[0]) and (b[0] <= c[0]):
            # print  "min = b[0]: ", b[0]
            mergedlst.append(b[0])
            b.remove(b[0])
            steps += 3
        elif (c[0] <= a[0]) and (c[0] <= b[0]):
            # print  "min = c[0]: ", c[0]
            mergedlst.append(c[0])
            c.remove(c[0])
            steps += 3
    # print  "lengths: ", len(a), len(b), len(c)
    # print  "mergedlst: ", mergedlst
    if len(a) == 0:
        return merge2(mergedlst,merge2(b,c))
    elif len(b) == 0:
        return merge2(mergedlst,merge2(a,c))
    elif len(c) == 0:
        return merge2(mergedlst,merge2(a,b))
    steps += 3
    # # print  "steps = ", steps
    return mergedlst


################# (2-WAY) MERGE SORT (REGULAR)   #######################

runtimes_merge2 = []
steps_merge2 = []

def mergesort2(lst):
    #divide and conquer - sort an array using merge sort algorithm
    #print "sorting:", lst
    global steps
    steps += 1
    if len(lst) <= 1:
        #print "base case!", len(lst)
        steps += 1
        return lst
    else:
        steps += 3
        half = len(lst)/2
        lefthalf = mergesort2(lst[:half])
        righthalf = mergesort2(lst[half:])
        #print "merging:", lefthalf, righthalf
        result = merge2(lefthalf,righthalf)
        #print "merged:", result
        return result

def timed_mergesort2(lst):
    global steps
    steps = 0
    start_time = time.time()
    result = mergesort2(lst)
    runtime = "%.10f" % (time.time()-start_time)
    runtimes_merge2.append(runtime)
    steps_merge2.append(steps)
    #print "time: %.2f seconds " %  runtime
    #print "steps:", steps
    return result

################# 3-WAY MERGE SORT (no insertion)   #######################

runtimes_merge3 = []
steps_merge3 = []


def mergedividesort3(lst):
    #divide and conquer - sort an array using merge sort algorithm
    global steps
    steps += 1
    # print  "sorting:", lst
    if len(lst) <= 2:
        #since list of length 2 is too small for 3 way merge sort
        # print  "base case! len(lst):", len(lst)
        if len(lst) <= 1:
            return lst
        elif lst[0]> lst[1]: #if list is unordered
             lst[0],lst[1] = lst[1],lst[0] #swap
             steps += 2
        steps += 1
        return lst
    else:
        third = int(len(lst)/3)
        steps += 1
        a = mergedividesort3(lst[:third])
        b = mergedividesort3(lst[third:(2*third)])
        c = mergedividesort3(lst[(2*third):])
        # print  "merging:", a, b, c
        result = merge3(a,b,c)
        # print  "merged:", result
        steps += 1
        return result


def timed_mergesort3(lst):
    #global steps
    #steps = 0
    start_time = time.time()
    result = mergedividesort3(lst)
    runtime = "%.10f" % (time.time()-start_time)
    runtimes_merge3.append(runtime)
    steps_merge3.append(steps)
    #print "time: %.2f seconds " %  runtime
    return result



############## MERGE SORT 3 WAY INCLUDING INSERTION SORT ###########

runtimes_merge3insert = []
runtimes_insertion = []
steps_merge3insert = []

def insertionsort(lst):
    start_insertion = time.time()
    global steps
    global runtimes_insertion
    for i in xrange(1, len(lst)):
        current = lst[i]  #saving the current item value for comparison as a separate variable
        k = i   #keeping the current index locator
        #backing up the current value its sorted position
        steps += 2
        while k > 0 and current < lst[k - 1]:
            lst[k] = lst[k - 1]
            k -= 1
            steps += 2
        lst[k] = current
    #print "steps: ", steps
    runtime = time.time() - start_insertion
    #print "time: ", runtime, "seconds"
    runtimes_insertion.append(runtime)
    return lst


def mergedividesort3_insertion(lst,k):
    #divide and conquer - sort an array using merge sort algorithm
    global steps
    steps += 1
    # print  "sorting:", lst
    if len(lst) <= k:
        insertionsort(lst)
    if len(lst) <= 2:
        #since list of length 2 is too small for 3 way merge sort
        # print  "base case! len(lst):", len(lst)
        if len(lst) <= 1:
            return lst
        elif lst[0]> lst[1]: #if list is unordered
             lst[0],lst[1] = lst[1],lst[0] #swap
             steps += 2
        steps += 1
        return lst
    else:
        third = int(len(lst)/3)
        steps += 1
        a = mergedividesort3_insertion(lst[:third],k)
        b = mergedividesort3_insertion(lst[third:(2*third)],k)
        c = mergedividesort3_insertion(lst[(2*third):],k)
        # print  "merging:", a, b, c
        result = merge3(a,b,c)
        # print  "merged:", result
        steps += 1
        return result


def timed_merge3_insertion_sort(lst,insertionmin):
    global steps
    global runtimes
    steps = 0 #restting steps
    start_time = time.time()
    result = mergedividesort3_insertion(lst,insertionmin)
    runtime = "%.10f" % (time.time()-start_time)
    runtimes_merge3insert.append(runtime)
    steps_merge3insert.append(steps)
    #print "time: %.2f seconds " %  runtime
    #print "steps:", steps
    return result


def run_experiments(insertionmin):
    #restting runtimes lists
    global steps, runtimes_merge2, runtimes_merge3, runtimes_merge3insert, runtimes_insertion
    runtimes_merge2, runtimes_merge3, runtimes_merge3insert, runtimes_insertion = [], [], [], []
    steps = 0
    exps = xrange(10)
    #try sorting lists of every length up to this length (of exps)
    for exp in exps:
        lst = [random.randint(-1000,1000) for r in xrange(exp)]
        #run merge3way-with-insertion-sort function
        timed_mergesort2(lst)
        timed_mergesort3(lst)
        timed_merge3_insertion_sort(lst,insertionmin)
        insertionsort(lst)
    print "runtimes_insertion: ", runtimes_insertion
    print "runtimes_merge2: ", runtimes_merge2
    print "runtimes_merge3: ",  runtimes_merge3
    print "runtimes_merge3insert:",  runtimes_merge3insert
    plt.plot(exps,runtimes_merge2,'g')
    plt.plot(exps,runtimes_merge3,'b')
    plt.plot(exps,runtimes_merge3insert,'r')
    #plt.plot(exps,runtimes_insertion,'w')
    plt.show()

def large_experiment(insertionmin):
    #restting runtimes lists
    global steps, runtimes_merge2, runtimes_merge3, runtimes_merge3insert, runtimes_insertion
    runtimes_merge2, runtimes_merge3, runtimes_merge3insert, runtimes_insertion = [], [], [], []
    steps = 0
    n = xrange(1000000)
    lst = [random.randint(-1000,1000) for _ in n]
    num_experiments = 50
    for repeat in (xrange(num_experiments)):
        timed_mergesort2(lst)
        timed_mergesort3(lst)
        timed_merge3_insertion_sort(lst,insertionmin)
    print "runtimes_insertion_million: ", runtimes_insertion
    print "runtimes_merge2_million: ", runtimes_merge2
    print "runtimes_merge3_million: ",  runtimes_merge3
    print "runtimes_merge3insert_million:",  runtimes_merge3insert
    plt.plot(n,runtimes_merge2,'g')
    plt.plot(n,runtimes_merge3,'b')
    plt.plot(n,runtimes_merge3insert,'r')
    #plt.plot(exps,runtimes_insertion,'w')
    plt.show()


#exps = xrange(100)
#for exp in exps:
#    lst = [random.randint(-1000,1000) for r in xrange(exp)]
#    insertionsort(lst)
#plt.plot(exps,runtimes_insertion,'w')
#plt.show()





###### TEST CASES #######

a = [3,7,2,1,4,0]
b = [0,6,2,9,-1,4]
c = [9,3]
d = [1000,3,7,2,1,4,0.5,0,6,2,9,-1,4,22,44,666,3,80349,0]
range = range(-1000,1001) #inverse 2000 numbers

#####RUN#####
#print insertionsort(ran)
#exps = xrange(100)
#print exps
#print run_experiments(10)
print large_experiment(3)
#print timed_mergesort2(range)
#print timed_mergesort3(range)
#print timed_merge3_insertion_sort(range,10)







