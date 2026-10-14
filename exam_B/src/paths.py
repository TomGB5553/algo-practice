


def grid_paths(rows, cols):
    if rows==1 or cols==1:
        return 1
    return grid_paths(rows-1, cols) + grid_paths(rows, cols-1)

def grid_paths_memo(rows, cols, cache=None):
    if rows==1 or cols==1:
        return 1
    
    if (rows-1, cols) in cache or (rows, cols-1) in cache :
        return cache[(rows-1, cols)] + cache[(rows, cols-1)]
    
    cache[(rows-1, cols)]= grid_paths(rows-1, cols)
    cache[(rows, cols-1)]= grid_paths(rows, cols-1)
    
    return cache[(rows-1, cols)] + cache[(rows, cols-1)]

def binary_strings(n):
    