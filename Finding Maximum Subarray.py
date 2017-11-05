#Maximum-subarray

#If we know the maximum-subarray for a given array
# and someone comes and adds a single extra integer,
# can we use our previous knowledge for a faster solution rather than just re-running everything?

#Write a function incremental_max_subarray(x, mx), where
#x is an array of integers
#mx is the max_subarray of x[0:-1],
#which then returns the max_subarray of the entire list.
# Give Big-O, Big-?, and Big-? bounds where possible.
# If you use any built-in python functions,
# be sure to take the complexity of those functions into account.

lst = [3,7,5,9,1,-4,5,-3,0,-3,2,-10,20,3,40,-100,60,-10]
def incremental_max_subarray(x, mx):
    mx =  max_subarray(x, mx) #max so far
    #I only want to add the new item if it's positive...
    if (x[-1] > 0):
        #and if the sum of the items between the end of previous max until the new item + the new item, combined, is positive
        if ( sum(x[(x.index(mx[-1])):])) > 0:
            mx = sum(x[(x.index(mx[-1])):])
            mx_indexes = [x.index(mx[-1]),-1]
    else:
        return max_subarray(x, mx)

def recursive_mx_subarray(A):
    if len(A) == 0:
        print "base case! len(list)=0"
        return (0, 0)
    (mx_subarray, mx_endarray) = recursive_mx_subarray(A[:-1])
    mx_endarray = max(mx_endarray + A[-1], 0)
    print "mx_endarray: ", mx_endarray
    mx_subarray = max(mx_subarray, mx_endarray)
    print "mx_subarray: ", mx_subarray
    return mx_subarray, mx_endarray


def mx_subarray(A):
    (x, _) = recursive_mx_subarray(A)
    return x

print mx_subarray(lst)