from time import time

def mem_cu_rod(p,n):
    res = {0 : 1, 1 : 1}
    def helper(n):
       print res
       if n <= 0:
          return 0
       # First check to see if the result has already been done
       if n in res:
           return res[n]
       elif n not in res:
          res[n] = max(q,p[i-1] + cut_rod_recursive(p,n-i))
       return res[n]
    return helper(n)



def opt_game_aug(arr):
    mems = {0:0}
    arrcopy = arr
    #we'll account for out step
    #and assuming any of 2 options of the opponent,
    #then OUR next choice; meaning, 2 turns forward
    def opt_game(arr):
        print arr
        print mems

        if type(arr) == int:
            print 'int'
            mems[arr] = arr
            return tuple(arr)

        if tuple(arr) in mems:
            return mems[tuple(arr)]
        else:
            if len(arr) <= 2:
                print 'small list <= 2'
                mems[tuple(arr)] = max(arr)
            else:
                print 'large list'
                gameoptions = []
                gameoptions.append(opt_game((arr[0]) + opt_game(arr[2:])))
                gameoptions.append(opt_game(arr[0] + opt_game(arr[1:-1])))
                gameoptions.append(opt_game(arr[-1] + opt_game(arr[1:-1])))
                gameoptions.append(opt_game(arr[-1] + opt_game(arr[:-2])))
                mems[tuple(arr)] = max(gameoptions)
        return mems[tuple(list)]
    return opt_game(arr)

#print opt_game_aug([2,10,1,5])



v = [15,2,10,1,5,8,4,6,1,7,3,7,2,5,11,2,14,6,2,5,8,23,5,4,3,23,65,87,1,2,3,76,3,98,54,2,4,5,6,4,2,46,8,9,4,2,4,5,67,8,4,2,23,4,3,45,7,8,6]
from time import time

start = time()

mem = {}
def opt_game(lst):
    #print lst
    if type(lst) == int:
        #print 'Integer'
        mem[lst] = lst
        return (lst)

    if tuple(lst) in mem:
        #print 'Sub-problem already solved'
        return mem[tuple(lst)]
    else:
        if len(lst) <= 2:
            #print 'Small list'
            mem[tuple(lst)] = max(lst)
        else:
            #print 'Large list'
            games = []
            games.append(opt_game(lst[0]+opt_game(lst[1:-1])))
            games.append(opt_game(lst[0]+opt_game(lst[2:])))
            games.append(opt_game(lst[-1]+opt_game(lst[1:-1])))
            games.append(opt_game(lst[-1]+opt_game(lst[:-2])))
            mem[tuple(lst)] = max(games)
    return mem[tuple(lst)]

print opt_game(v)

print time() - start



def max_coin_game_value(values):
  results = {}
  def helper(values):
    if values not in results:
      if len(values) < 3:
        results[values] = max(values)
      else:
        results[values] = max(values[0]  + helper(values[1:-1]), \
                              values[0]  + helper(values[2:  ]), \
                              values[-1] + helper(values[ :-2]), \
                              values[-1] + helper(values[1:-1]))
    return results[values]
  return helper(tuple(values))


print max_coin_game_value([2, 10, 1, 5])


def dijkstra(edges,vertices,end, starting,base_values):

    vertices[end] = 1
    current = end
    visited = []
    while len(visited) < len(vertices):
        visited.append(current)
        current_dist = vertices[current]
        for edge in edges:
            if edge.n2 == current and edge.n1 not in visited:
                if current == end:
                    dist = (float(1)/float(edge.weight))
                else:
                    dist = (float(vertices[current])/float(edge.weight))
                if edge.n2 != start:
                    us_dist = dist*(float(1)/float(base_values[edge.n1]))
                else:
                    us_dist = dist
                if (us_dist) < vertices[edge.n1]:
                    vertices[edge.n1] = dist

        minimum = ('node',inf)
        for node in vertices:
            if node != start:
                us_dist = vertices[node]*(float(1)/float(base_values[edge.n1]))
            else:
                us_dist = vertices[node]
            if us_dist < minimum[1] and node not in visited:
                minimum = (node,us_dist)

        current = minimum[0]
    return vertices
