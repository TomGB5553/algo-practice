

# python_slicing_summary.py

# The anatomy of a slice: my_list[start:stop:step]
# start: inclusive (defaults to 0)
# stop: exclusive (defaults to end of list)
# step: interval (defaults to 1)

letters = ['a', 'b', 'c', 'd', 'e', 'f']
print(f"Original list: {letters}\n")

# 1. Basic Slicing ([start:stop])
# Gets items from index 1 up to (but not including) index 4
print("1. Basic Slicing      [1:4]  ->", letters[1:4])

# 2. Omitting Start ([:stop])
# Defaults to the beginning of the list
print("2. Omitting Start     [:3]   ->", letters[:3])

# 3. Omitting Stop ([start:])
# Defaults to the end of the list
print("3. Omitting Stop      [3:]   ->", letters[3:])

# 4. Omitting Both ([:])
# Creates a shallow copy of the entire list
print("4. Omitting Both      [:]    ->", letters[:])

# 5. Using Step ([start:stop:step] or [::step])
# Extracts elements at specific intervals
print("5. Using Step         [::2]  ->", letters[::2])

# 6. Negative Indices
# Counts backward from the end of the list (-1 is the last item)
print("6a. Negative Start    [-3:]  ->", letters[-3:])
print("6b. Negative Stop     [:-1]  ->", letters[:-1])

# 7. Reversing a List
# A negative step moves backward through the list
print("7. Reversing          [::-1] ->", letters[::-1])
