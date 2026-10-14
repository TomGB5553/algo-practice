# Exercise 2 : write your functions here (catalan, catalan_memo, catalan_iter)
from typing import Optional
from typing import Dict

    
def catalan(n: int, cache: Optional[Dict[int, int]] =None):
    """_summary_

    Args:
        n (int): _description_
        cache (Optional[Dict[int, int]], optional): _description_. Defaults to None.

    Returns:
        int: _description_
    """
    result=0
    if n==0:
        return 1
    if n in cache:
        return cache[n]
    for i in range(n):
        result += catalan(i, cache)*catalan(n-1-i, cache)
    return result

print(catalan(3))


def catalan_iter(n: int) -> int:
    values=[1]
    for k in range(1, n+1):
        total=0
        for i in range(n):
            total += values[i]+values[k-1-i]
        values.append(total)
    return values[n]

