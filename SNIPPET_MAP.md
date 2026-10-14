# Snippet map : "I need X in the exam, where is my code?"

You will have access to your projects during the exam. This map tells you where each pattern is
(all the files are commented, with the syntax explained). Paths are from `algorithm-and-computing-class/`.

| I need to...                                              | Open this file | Function / class |
|-----------------------------------------------------------|----------------|------------------|
| write a class with `__init__`, `__repr__`, `__lt__`        | `projects/celestial-mechanics/neos/neo.py` | `NearEarthObject` |
| write `__add__` / `__mul__` returning a new object         | `projects/celestial-mechanics/celestial/vec3.py`, `projects/basics-of-algorithmic/src/fibo.py` | `Vector3d.__add__`, `Matrix.__mul__` |
| inheritance + `super().__init__`                           | `projects/trees/bst/tree.py` | `BinarySearchTree` |
| a class that analyses a list (average, count)              | `projects/celestial-mechanics/neos/neo_analyzer.py` | `NeoAnalyzer` |
| read a JSON file                                           | `projects/flight-analysis/src/airports.py` | `load_airports` |
| read a nested JSON, build a flat list of objects           | `projects/celestial-mechanics/neos/data_reader.py` | `read_neos_from_json` |
| read a CSV file (DictReader)                               | `projects/flight-analysis/src/flights.py` | `load_flights` |
| count with a dict (by state, by carrier...)                | `projects/flight-analysis/src/airports.py`, `flights.py` | `get_number_of_airports_by_state`, `get_number_of_flights_by_carrier` |
| average / ratio per category + sort a list of dicts        | `projects/flight-analysis/src/flights.py` | `get_ranked_carriers_by_on_time_performance`, `get_on_time_performance_by_airports` |
| find the best / the maximum with a loop                    | `projects/language-detection/src/occurrence_frequencies.py` | `detect_language` |
| filter a list with conditions                              | `projects/celestial-mechanics/neos/neo_filter.py` | `filter_neos` |
| frequencies of letters, probability / log formulas         | `projects/language-detection/src/occurrence_frequencies.py` | `compute_occurrence_frequencies`, `kl_divergence` |
| random excerpt, repeat an experiment, average              | `projects/language-detection/src/text_length.py` | `detection_accuracy_for_length` |
| plot with matplotlib (axes, legend, log scale)             | `projects/language-detection/detection_accuracy.py`, `projects/basics-of-algorithmic/fibo_time.py` | |
| time a function                                            | `projects/basics-of-algorithmic/fibo_time.py`, `sorting_time.py` | `timeit` |
| recursion, memoization (cache dict)                        | `projects/basics-of-algorithmic/src/fibo.py` | `fibo`, `fibo_memo` |
| iterative version of a recursion                           | `projects/basics-of-algorithmic/src/fibo.py` | `fibo_iter` |
| exponentiation by squaring                                 | `projects/basics-of-algorithmic/src/fibo.py` | `power` |
| bubble / selection / quick / merge sort                    | `projects/basics-of-algorithmic/src/sort.py` | |
| sort with a `key` function                                 | `projects/basics-of-algorithmic/src/generic_sort.py` | |
| stability of a sort, sort by two criteria                  | `projects/basics-of-algorithmic/src/stability.py`, `main_two_criteria.py` | `is_stable` |
| linear / binary search                                     | `projects/trees/bst/search.py` | `linear_search`, `binary_search` |
| binary tree, 4 traversals, BFS with a queue                | `projects/trees/bst/tree.py` | `BinaryTree` |
| BST insert / find / min / max / delete                     | `projects/trees/bst/tree.py` | `BinarySearchTree` |
| Euler integration, simulation loop                         | `projects/celestial-mechanics/celestial/simulation.py` | `simulate` |
| priority queue / heap, dict-based coding                   | `projects/trees/huffman/huffman.py` | `build_huffman_tree` |
| anything about syntax                                      | `learn-python/notebooks/01 ... 09` and `CHEATSHEET.md` | |

Tip: during the exam, do not copy blindly. Open the file, re-read the explanation comment, and ADAPT it
(names, keys, the exact return type asked by the statement).
