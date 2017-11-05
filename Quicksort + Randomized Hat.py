""" giving random hats to random people, how many people will get their original hat back?
"""
from random import shuffle, choice, randrange
import matplotlib.pyplot as plt
from numpy import mean, median
from time import time
def hat_random_returns(n):
    people_keys = range(n)
    #print people_keys
    hat_keys = range(n)
    shuffle(hat_keys)
    #print hat_keys
    correct_hats = 0
    for i in range(n):
        people_keys[i]== hat_keys[i]
        if people_keys[i]== hat_keys[i]:
            correct_hats += 1
    return correct_hats

def exp_hats():
    correct_hats_results = []
    for n in range(1000):
        correct = []
        for exp in range (30):
            correct.append(hat_random_returns(n))
        correct_hats_results.append(mean(correct))

    plt.plot(range(1000),correct_hats_results)
    plt.show()


#probablity of each person to get their hat is 1/n
#for n runs, how many people would get their hat? this is (1/n)*n = 1

#exp_hats()

def gorilla_worst_shuffle_sort(lst):
    n = len(lst)
    counter = 0
    while lst != list.sort():
        shuffle(lst)
        counter+=1
    return counter, n

#approx median finder
def approx_median_finder(lst,delta):
    truemedian = median(lst)
    selectinglst = lst
    med = choice(selectinglst)
    while (med < (truemedian-delta*truemedian/2) or med > (truemedian+delta*truemedian/2)) and selectinglst:
        print "med: %.2f, (truemedian-delta/2: %.3f), (truemedian+delta/2): %.3f" % (med, (truemedian-delta*truemedian/2) , (truemedian+delta*truemedian/2))
        med = choice(selectinglst)
        selectinglst.remove(med)
    return med

#print approx_median_finder([1,2,3,4,5,6,7,8],0.5)



######BOOK_QUICKSORT######
def bookpartition(lst,p,r):
    pivot = lst[r]
    i = p-1
    j = p
    print lst[p:r]
    print pivot,p,j
    for _ in lst[j:r]:
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[r] =  lst[r] , lst[i+1]
    return i+1
def boookquicksortelegant(lst,p,r):
    if p<r:
        mid = partition(lst,p,r)
        print lst[p:r]
        quicksortelegant(lst,p,mid-1)
        print lst[p:mid-1], lst[mid+1:r]
        quicksortelegant(lst,mid+1,r)
    print lst
    return lst
def bookquicksortinitialelegant(lst):
    quicksortelegant(lst,0,(len(lst)-1))



######QuickSort######

def partition(array, start, end):
    pivot = start
    for item in range(pivot+1, end+1):
        if array[item] <= array[start]:
            pivot += 1
            array[item], array[pivot] = array[pivot], array[item]
    array[pivot], array[start] = array[start], array[pivot]
    return pivot


def quicksort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1
    if start >= end:
       print array
        return array
    sortedarray = sorted(array)
    print "sortedarray: ", sortedarray
    if array == sortedarray:
        return array
    pivot = partition(array, start, end)
    quicksort(array, start, pivot-1)
    quicksort(array, pivot+1, end)
    print array
    return array



##inputs###
import random
smallist = range(20,0,-1)
randlist =  [random.random() for a in range(100000)]
ordlsit = range(100000)

#print quicksort(smallist)
#####RANDOMIZED QUICKSORT###### 
 
 
 
def swap( A, x, y ):
  A[x],A[y]=A[y],A[x]
  
def quicksortWrapper( array ):
    quicksort( array, 0, len( array ) - 1 )
 
 
 
def partition( array, left, right ) :
    pivot = left + random.randrange( right - left + 1 )
    swap( array, pivot, right )
    for i in range( left, right ):
      if array[i] <= array[right]:
        swap( array, i, left )
        left += 1
    swap( array, left, right )
    return left
 
 
def quicksort( array, left, right ):
    if left < right:
      pivot = partition( array, left, right )
      quicksort( array, left, pivot - 1 )
      quicksort( array, pivot + 1, right )


####FOBONACI#####
def fib(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
print fib(10)

def timefib(n):
    starttime = time()
    fib(n)
    endtime = time()
    runtime = endtime-starttime
    print n
    return runtime

def timefibrepeats(n,repeats):
    runtimes = []
    for repeat in range(repeats):
        runtimes.append(timefib(n))
    avgruntime = mean(runtimes)
    minruntime = min(runtimes)
    maxruntime = max(runtimes)
    print "runtimes between: %.8f seconds to %.8f seconds" % (minruntime, maxruntime)
    print "avg runtime: %.8f seconds" % avgruntime
    print runtimes

timefibrepeats(100,35)
