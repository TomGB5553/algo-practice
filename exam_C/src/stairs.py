# Exercise 2 : write your functions here (ways, ways_memo, ways_iter, stirling2)

def ways(n: int) -> int:
    if n<0:
        return 0
    if n==0:
        return 1
    return ways(n-1) + ways(n-2) + ways(n-3) 
    
def ways_memo(n: int, cache=None) -> int:
    if cache is None:
        cache={}                #attention EMPTY CACHE !
    if n<0:
        return 0
    if n==0:
        return 1
    if n in cache:
        return cache[n]
    cache[n] = ways_memo(n-1, cache) + ways_memo(n-2, cache) + ways_memo(n-3, cache)     #ATTENTION change function name to new
    return cache[n]                                                                        # ne pas oublier le cache dans args

def ways_iter(n: int) -> int:
    out=[1]
    
    
def stirling2(n: int, k: int, cache=None) -> int:
    if cache is None:
        cache={}
    if n==0 and k==0:
        return 1
    if n==0 or k==0:
        return 0
    key = (n, k)
    
    if key in cache:        #do not forget to check in cache !
        return cache[key]
    out=k * stirling2(n-1, k, cache) + stirling2(n-1, k-1, cache)       #do not forget the cache argument
    cache[(n,k)] = out
    return out 
    