###BLOOM FILTER####   Tomer Eldor #http://www.codeskulptor.org/#user42_GqQIvMJkvqfnjpV_0.py
import hashlib
from math import log
import matplotlib.pyplot as plt

#starting by defining helper HASHing function:
def hash(x):
    #hashing the function using sha1 function (relaible, less collisions and vulnurabilities than MD5, but similar running time).
    # **I took the running time and learned python implementation of it from Todorov, 2013 (http://atodorov.org/blog/2013/02/05/performance-test-md5-sha1-sha256-sha512/)
    h = hashlib.sha1(x).hexdigest()
    #the hash function is hexadecimal, meaning it uses 16base (including letters)
    # but we need index of only integers (until the max size of the bloom filter).
    # we convert to ints by hexadecimal numbers, then capping at the maximum size using modulo
    return int(h,base=16)

### Bloom Filter infrastructure ###
class Bloom:
    def __init__(self,data,fp):
        #my implementation lets the user insert the data and choose the desired false positive rate, as this is a more subjective paramter (and intuitive) that should be the one for the discresion of the user.

        n = len(data) #n = number of elements
        m = abs(int(round( (-n * log(fp)) / (log(2))**2 ))) #math formula to calculate optimal m as function of false positive rate

        self.size = m #size of the vector (m)
        self.vector = [0]*m #initializing the 'bit_vector' itself as an array of 0'z

        #k is defined as -m*ln(2)/n
        self.k = int(round(m * log(2)/n))#number of hash functions
        #print "optimal number of hash functions: ", self.k

        #initializing a parallel data array:
        #this is not part of the bloom filter itself, but rather my way for checking eventually the false positives rate
        # for the last question in the assignment. This should not be considered as an actual part of the bloom filter
        self.dataaraay = [] # reserving a list with all keys we truly inserted, for checking false positives
        for element in data:
            self.insert(element)



    #inserting into bloom filter:
    def insert(self,key):
        #only for checking false positive rate (last question), I'm also storing the keys in a dataset that I can later lookup at:
        self.dataaraay.append(key)
        #now, for the search:
        #method for generating as many hashes as k:
        # concatenating an "i" - an incrementing int up to k,
        # to the end of the key we wanted to insert, before hashing it
        # Thus we have k different hashes - each of them is the key + i (up to k)
        for i in range(self.k):
            curr_key = str(key)+str(i) #adding i to the key
            index =  ( hash(curr_key) % self.size ) #finding index by hashing current key (+i), capping by size
            #set the index equal to the hash functions to 1:
            self.vector[index] = 1

    #querying: checking if key is (probably) in the dataset:
    def search(self,key):
        #similarly, in searching for the key, we need to find all indexes of the key + i (each i  up to k)
        for i in range(self.k):
            curr_key = str(key)+str(i) #adding i to the key
            index =  ( hash(curr_key) % self.size )  #finding index by hashing current key (+i), capping by size
            if self.vector[index] == 0:
                return False # the key doesn't exist
        return True #although it is only PROBABLY true!

    ########################
    #this is only for
    def verify(self,key):
        #if we have a "probably yes" bloom filter result:
        if self.search(key):
            #checking if key was actually inserted in the process:
            if key in self.dataaraay: #true positive
                return False
            else: #false positive!
                #print "False Positive!", key
                return True
        else: #true negative
            return False


#############



#b.insert('kaboom')
#for i in xrange(50):
#    b.insert(('str'+str(i)))
#    b.insert(i)

def false_pos_rate(originaldata, verifying_dataset,k):
    #initialize bloom filter
    b = Bloom(originaldata,k) #inserting numbers from 0 to 99.
    #verify the following values to check for false positives:
    falsepositives = 0
    #verifying_dataset = xrange(99,1000)
    for i in verifying_dataset:
        if b.verify(i):
            falsepositives += 1

    false_positive_rate =  float(falsepositives)/len(verifying_dataset)
    return false_positive_rate #returning the false positive rate


####plot!#####
def plot_false_pos_rate(test_ns,k):
    #initialize bloom filter
    #verify the following values to check for false positives:
    fps = []
    for n in test_ns:
        fps.append(false_pos_rate(xrange(n), xrange(n,100000+n),k))
    plt.figure()
    plt.title('False positive rate with scale')
    plt.xlabel("n - # elements inserted ")
    plt.ylabel("False positive rate")
    #plotting estimationm and difference as proportion from pi
    #plotting real value of pi, and 0 to compare)
    plt.plot(test_ns,fps, color='green', label='False positive rate by n')
    #plt.plot(ks,fps, color='blue', label='False positive rate by k')
    plt.legend(fancybox=True)
    plt.show()
    return fps


#######!!!LET'S RUN IT!!!######

test_ns = [50,100,500,1000,2000,3000,4000,5000]
#try these ns with that false positive rate, let's see what fp rate actually exists!
print plot_false_pos_rate(test_ns, 0.05)
