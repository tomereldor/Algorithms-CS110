import time

#####insertion sort##### - takes item, check if it's smaller than previous,
# shifts everything forward by one and places the item where stopped (before all the bigger items)
def insertion_sort(list):
    print "Insertion Sorting:", list
    start_time = time.time()
    counter = 0

    ##insertion_sort##
    for i in range(1,len(list)):
        counter += 1 #count step
        tmp = list[i]
        while i>0 and tmp < list[i-1]:
            #check against our current value (tmp) all previous values
            counter += 1 #count steps
            #switch positions:
            list[i] = list[i-1]
            i -= 1
        #and place our current value before the first bigger item
        list[i] = tmp
    runtime_insertion = time.time() - start_time
    print counter + 2, "steps"
    print list
    print "--- %s seconds ---" % runtime_insertion
    return list, runtime_insertion, counter

list1 = [11,03,1-5,4,2,68,45,743,2,46,3,342,-5,622,-0.5]
insertion_sort(list1)


######SELECT SORT###### - selects item, searches for minimum, swaps item with minimum


def selection_sort(list):
    print "Selection Sorting:", list
    start_time = time.time()
    counter = 0
    for index in range(len(list)):
        counter += 1
        min = list[index]
        minposition = index
        for j in range(index+1,len(list)):
            counter += 1
            if list[j] < min:
                counter += 1
                min = list[j]
                minposition = j
        list[minposition] = list[index]
        list[index] = min
    end_time = time.time()
    runtime_selection = end_time - start_time
    print list

def insertion_sort(list):
    print "Insertion Sorting:", list
    start_time = time.time()
    counter = 0

    ##insertion_sort##
    for i in range(1,len(list)):
        counter += 1 #count step
        tmp = list[i]
        while i>0 and tmp < list[i-1]:
            #check against our current value (tmp) all previous values
            counter += 1 #count steps
            #switch positions:
            list[i] = list[i-1]
            i -= 1
        #and place our current value before the first bigger item
        list[i] = tmp
    runtime_insertion = time.time() - start_time
    print counter + 2, "steps"
    print list
    print "--- %s seconds ---" % runtime_insertion
    return list, runtime_insertion, counter

list1 = [11,03,1-5,4,2,68,45,743,2,46,3,342,-5,622,-0.5]
insertion_sort(list1)


######SELECT SORT###### - selects item, searches for minimum, swaps item with minimum


def selection_sort(list):
    print "Selection Sorting:", list
    start_time = time.time()
    counter = 0
    for index in range(len(list)):
        counter += 1
        min = list[index]
        minposition = index
        for j in range(index+1,len(list)):
            counter += 1
            if list[j] < min:
                counter += 1
                min = list[j]
                minposition = j
        list[minposition] = list[index]
        list[index] = min
    end_time = time.time()
    runtime_selection = end_time - start_time
    print list
    print "steps: ", counter+3
    print "--- Selection sort took %s seconds ---" % runtime_selection
    return list, runtime_selection, counter

selection_sort(list1)



#Bubble sort take O(n^2) time.


from random import randint
def rand_list(m):
    lst = []
    for _ in xrange(m):
        lst.append(int(randint(-1000, 1000)))
    return lst


list2 = range(0,100,1)
print "list2:", list2
list3 = range(100,0,-1)
print "list3:", list3


#__________NOT MINE - FROM WEB = SHORTER - divided to swap function__________:#
def selectionsortweb(aList):
    for i in range( len( aList ) ):
        least = i
        for k in range( i + 1 , len( aList ) ):
          if aList[k] < aList[least]:
            least = k
        swap( aList, least, i )
    return aList

def swap( list, x, y ):
  tmp = list[x]
  list[x] = list[y]
  list[y] = tmp