#Cuckoo Hashing

m = 100 #size
table = "":"" for xrange(m) in {}
def hash1(x): return x^(1-x) % m
def hash2(x): return x^(1/x) % m

def cuckoohash(table,x):
    m = len(table)
    index = hash1(x)
    #if index is full:
    if table(index) != None:
        index = hash2(x)
        if table(index) != None:
            raise ValueError
    return index

def cuckooinsert(table,x)
    table[cuckoohash(table,x)] = x

def lookup(table,x):
    table[cuckoohash(table,x)] == x



#######################
class Cuckoo:
    def __init__(self,funcs,tableSize,maxDepth):
        self.table = [None]*tableSize
        self.funcs = funcs
        self.excess = []
        self.maxDepth = maxDepth
        self.size = tableSize

    def insert(self,key):
        if Cuckoo.find(self, key) != None: # if key exists
            return None
        # key doesn't exist
        min_insert_way = Cuckoo.insert2(self, key, [], 0)
        if min_insert_way[0] == -1: # if we can't commit max 3 replacement
            self.excess.append(key)
            return -1
        # we can commit max 3 replacement
        i = len(min_insert_way) - 1
        orginal_place = self.funcs[min_insert_way[-1]] (key,self.size) # it is the index of key in which it entered
        while ( i>=0 ):
            function_index = min_insert_way[i]
            replaced_element = self.table[self.funcs[function_index](key, self.size)]
            self.table[self.funcs[function_index](key, self.size)] = key # we replace he replaced element with key
            key = replaced_element
            i = i - 1
        return orginal_place

    def insert2(self, key, way, displacements):
        '''
        the function get 4 parameters:
        1. self == the hash table
        2. key
        3. way which is in the begging: way == []
        4. displacements == how many self.funcs have used

        the function return the way in which the insert will be. "way" is list of indexes of the self.funcs in which we do the insert
        for exmple, if way == [2,3], we will put "key" in self.table[self.funcs[3]] instead of "replaced_element".
        then, we will put "replaced_element" in self.table[self.funcs[2]].
        as you can see, the indexes are from the right to the left.
        if we have to use self.excess: way == [-1, X(1), X(1), ... X(max_depth)]
        '''
        if (displacements > self.maxDepth): # if we couldn't find max 3 displacements
            return [-1]
        for i in range(0, len(self.funcs)):
            if self.table[self.funcs[i](key,self.size)] == None: # if one of the functions gives empty place
                return [i]
        # there is no an empty place
        replaced_element = self.table[self.funcs[0](key,self.size)] # "replaced_element" will be replaced by "key"
        min_way = Cuckoo.insert2(self, replaced_element, way, displacements+1)
        min_way.append(0) # because we have used self.funcs[0]
        for i in range (1,len(self.funcs)):
            replaced_element = self.table[self.funcs[i](key,self.size)] # "replaced_element" will be replaced by "key"
            current_way = Cuckoo.insert2(self, replaced_element, way, displacements+1)
            current_way.append(i) # because we have used h(i)
            if len(current_way) < len(min_way):
                min_way = current_way
        return min_way