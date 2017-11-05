from matplotlib import rc
import matplotlib.pyplot as plt
import numpy as np
import random
import string

#plt.style.use('seaborn-deep')
# whatever size you want your figure to be
plt.rcParams['figure.figsize'] = 14, 8
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['grid.color'] = 'lightgray'

font = {
    'family': 'serif',
    'serif': ['Palatino'],
    'size': 20
}
rc('font', **font)

def randomword(length):
    return ''.join(random.choice(string.lowercase) for i in range(length))

def empty_hash_table(N):
    return [[] for _ in xrange(N)]

def add_to_hash_table(hash_table, item, hash_function):
    N = len(hash_table)
    # Fill me in
    index = (hash_function(item) ) % N
    #if index > N:
    #    index = (index % N)
    hash_table[index].append(item)
    return hash_table


def contains(hash_table, item, hash_function):
    N = len(hash_table)
    # Fill me in
    index =  hash_function(item) % N
    return (item in hash_table[index])
    # Return true if `item` is in `hash_table`


def remove(hash_table, item, hash_function):
    if not contains(hash_table, item, hash_function):
        raise ValueError()
    # Fill me in
    index = hash_function(item) % len(hash_table)
    hash_table[index].remove(item)
    return hash_table


def hash_str1(string):
    ans = 0
    for chr in string:
        ans += ord(chr)
    return ans


def hash_str2(string):
    ans = 0
    for chr in string:
        ans = ans ^ ord(chr)
    return ans


def hash_str3(string):
    ans = 0
    for chr in string:
        ans = ans * 128 + ord(chr)
    return ans


def hash_str4(string):
    random.seed(ord(string[0]))
    return random.getrandbits(32)


# Initialize
words = [randomword(10) for _ in xrange(100000)]
table1 = empty_hash_table(5000)
table2 = empty_hash_table(5000)
table3 = empty_hash_table(5000)
table4 = empty_hash_table(5000)
table = [table1, table2, table3, table4]
hashes = [hash_str1, hash_str2, hash_str3, hash_str4]

# Add words to tables
for w in words:
    for (t, f) in zip(table, hashes):
        add_to_hash_table(t, w, f)

# Get the size of each bucket for each table
bucket_sizes = [[] for _ in xrange(4)]
for (i, t) in enumerate(table):
    for slot in t:
        bucket_sizes[i].append(len(slot))

# Some basic stats about our buckets
for (i, b) in enumerate(bucket_sizes):
    print "Table", i+1, "has", len([x for x in b if x == 0]), "empty buckets."
    print "Table", i+1, "has average bucket size:", np.mean([x for x in b if x != 0])

# Plotting
for (i, b) in enumerate(bucket_sizes):
    plt.plot(range(1, len(b)+1), b, label = 'table ' + str(i + 1))
plt.legend()
plt.xlabel('Bucket #')
plt.ylabel('Size')
plt.show()

# PROFILING
import cProfile

def find_all(hash_table, items, hash_function, debug = False):
    for x in items:
        if not contains(hash_table, x, hash_function) and debug:
            print "Should not see this! Check element:", x

# Time finding elements in the table
cProfile.run('find_all(table1, words, hash_str1)')
# cProfile.run('find_all(table2, words, hash_str2)')
# cProfile.run('find_all(table3, words, hash_str3)')
# cProfile.run('find_all(table4, words, hash_str4)')


# Time finding elements not in the table
random_words = [randomword(4) for _ in xrange(100000)]
cProfile.run('find_all(table1, random_words, hash_str1)')
# cProfile.run('find_all(table2, random_words, hash_str2)')
# cProfile.run('find_all(table3, random_words, hash_str3)')
# cProfile.run('find_all(table4, random_words, hash_str4)')


