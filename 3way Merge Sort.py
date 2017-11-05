#Merge sort 3way with steps and time:
import time

steps = 0

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
    global steps
    steps = 0
    start_time = time.time()
    result = mergedividesort3(lst)
    print "time: %.2f seconds " %  (time.time()-start_time)
    print "steps:", steps
    return result


###### TEST CASES #######

a = [3,7,2,1,4,0]
b = [0,6,2,9,-1,4]
c = [9,3,45,8,-3,-0.2]
ab = [3,7,2,1,4,0.5,0,6,2,9,-1,4]
ran = range(-1000,1001) #inverse 2000 numbers

#####RUN#####
print timed_mergesort3(ran)
#steps =  25726
#time:  ~0.03-0.06
#print merge3([1,5],[4,-1],[6,2])

#from tqdm import tqdm
#    for repeat in tqdm(xrange(num_experiments)):






