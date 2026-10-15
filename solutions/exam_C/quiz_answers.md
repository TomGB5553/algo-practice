# Answer key of the quiz of mock exam C

1. **C** - [1, 2, 3, 4]  
   _`y = x` gives a second NAME to the same list, so `y.append(4)` changes what `x` shows too. A copy needs `x[:]` or `list(x)`._
2. **C** - return sorted(l)  
   _`sorted(l)` builds a new list. `l.sort()` modifies the caller's list and returns `None`; `list` has no `sorted` method._
3. **A** - "7"  
   _A loop on a dict gives the KEYS (strings here). Use `data[x]` for the value, or `.items()` for both._
4. **B** - return self.length() < other.length()  
   _A method is called with a dot on an object, with no argument for `self`. `self < other` would call `__lt__` again forever._
5. **B** - self.items = list(items)  
   _`list(items)` (or `items[:]`) builds a new list. `self.items = items` only creates a second name for the caller's list._
6. **A** - Error  
   _`cache` is `None` by default, so `n in cache` raises `TypeError: argument of type 'NoneType' is not iterable`. The fix is `if cache is None: cache = {}` at the start of the function._
7. **D** - O(n * k)  
   _There are at most n * k different pairs, each computed once with a constant number of operations: O(n * k)._
8. **B** - IndexError  
   _At k = 1 the list `values` has ONE element, so `values[k - 2]` is `values[-1]` (valid, the last element) but `values[k - 3]` is `values[-2]`, which does not exist: IndexError. Negative indices count from the end but must still exist. Handle the first values with `if k >= 2:` / `if k >= 3:`._
9. **A** - None  
   _`sort()` sorts in place and returns `None`. Write `return sorted(names)`._
10. **D** - Divide the total by 2  
   _Ignored means not counted: the divisor is the number of days actually found (2). Return `None` only if that number is 0._
