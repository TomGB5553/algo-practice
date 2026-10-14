# Answer key of the practice quiz

1. **B** - 4  
   _append adds ONE element (here a list) at the end. extend would add 4 and 5 separately._
2. **B** - d = {"a": 1}  
   _{key: value} is a dict; {a, b} is a set._
3. **C** - [20, 30]  
   _A slice goes from the start index (included) to the end index (EXCLUDED)._
4. **C** - 0  
   _get(key, default) returns the default instead of raising an error._
5. **B** - 3 and 1  
   _// is the integer division, % the remainder._
6. **C** - None  
   _Without return, a function returns None._
7. **B** - sort() sorts in place and returns None; sorted() returns a new sorted list  
   _A classic source of `None` bugs._
8. **B** - False, because strings are compared character by character and "9" > "1"  
   _Convert with int() BEFORE comparing._
9. **B** - without self, count is a local variable (or an error), the attribute is not changed  
   _Attributes are always accessed through self._
10. **B** - __str__ if it exists, else __repr__  
   _In the exam you were asked for __repr__._
11. **B** - a.__add__(b)
12. **C** - O(log n)  
   _i doubles at each turn: about log2(n) turns._
13. **C** - O(n^2)  
   _The dominant term is n^2 (the single loop is only n)._
14. **D** - O(2^n)  
   _Each call makes two calls and the same values are recomputed._
15. **C** - quick sort  
   _Quick sort: bad pivots (e.g. already sorted list + last-element pivot) give n^2._
16. **A** - it needs the list to be sorted
17. **C** - 10  
   _4 + 3 + 2 + 1 + 0 = 10._
18. **C** - postfix (post-order)
19. **B** - 1 3 4 5 8  
   _Infix on a BST always gives the values in ascending order._
20. **B** - the same list: the caller's list IS modified  
   _Lists are mutable and passed by reference: copy with list(l) if you must not modify it._
