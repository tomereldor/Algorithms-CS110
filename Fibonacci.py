I"""
Fibonacci numbers
In session 5.2, you analyzed the following version of Fibonacci:

def fib(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

In the spirit of the rod-cutting examples given in the textbook, write your own memoized version of Fibonacci, and a bottom-up version.
Rod-cutting without dynamic programming
"""
"""
1)
Implement CUT-ROD(p, n) in python code (NB - not the dynamic programming version)
Time the function for different values of n.
Plot the results.
Estimate how big n has to be before it will take a million years to finish. (Call this value: N, and use it in the next section)
"""
def cut_rod_recursive(p,n):
    if n == 0:
        return 0
    q = 0
    for i in xrange(1,n+1):
        q = max(q,p[i-1] + cut_rod_recursive(p,n-i))
    return q

print cut_rod_recursive([10,20,33,45,58,69,105,11],8)

"""
2)
Rod-cutting with dynamic programming
Implement PRINT-CUT-ROD-SOLUTION(p, n) in python code
Time the function for different values of n.
Plot the results on the same plot as the non-dynamic programming solution.
Estimate (or time) how long does it take to evaluate PRINT-CUT-ROD-SOLUTION(p, N)? (Where N is the value you got from the previous section)
Do you notice anything about the solution for large n?
"""

def memoized_cut_rod(p,n):
    r = range(n)
    for i in range(n):
        r[i] = None
    return memoized_cut_rod(p,n,r)

def memoized_cut_rod_AUX(p,n,r):
    if r[n] >= 0:
        return r[n]


def mem_fib(n):
    res = {0 : 1, 1 : 1}
    def helper(n):
       print res
       if n <= 0:
          return 0
       # First check to see if the result has already been done
       if n not in res:
          res[n] = helper(n-1) + helper(n-2)
       return res[n]
    return helper(n)


def mem_cu_rod(p,n):
    res = {0 : 1, 1 : 1}
    def helper(n):
       print res
       if n <= 0:
          return 0
       # First check to see if the result has already been done
       if n not in res:
          res[n] = max(q,p[i-1] + cut_rod_recursive(p,n-i))
       return res[n]
    return helper(n)

print mem_fib(10)