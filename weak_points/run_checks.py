"""
Check your answers to the weak-points exercises.

    python3 weak_points/run_checks.py            # all the exercise files
    python3 weak_points/run_checks.py ex3        # one file (ex1 ... ex6)
    python3 weak_points/run_checks.py ex4 -v     # show the full error traceback

(The maintainer can check the solutions with:  python3 weak_points/run_checks.py --solutions)
Each line says OK / FAIL / TODO (function still raises NotImplementedError). Read the FIRST FAIL only.
"""
import copy
import importlib.util
import os
import sys
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))
SOLUTIONS = os.path.join(os.path.dirname(HERE), "solutions", "weak_points")


def load(name, folder):
    path = os.path.join(folder, name + ".py")
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def unchanged(value, action):
    """Run action(value_copy_passed) and check the caller's value was not modified."""
    before = copy.deepcopy(value)
    result = action(value)
    assert value == before, "the input was MODIFIED but the statement says it must not be"
    return result


# =============================================================================================
# CHECKS : one function per exercise function, named check_<function name>
# =============================================================================================
# ---------------------------------------- ex1 ----------------------------------------
class Ex1:
    @staticmethod
    def indices_of(m):
        assert m.indices_of([5, 7, 5, 5], 5) == [0, 2, 3]
        assert m.indices_of([1, 2], 9) == []

    @staticmethod
    def dot_product(m):
        assert m.dot_product([1, 2, 3], [4, 5, 6]) == 32
        assert m.dot_product([], []) == 0

    @staticmethod
    def last_nonzero_index(m):
        assert m.last_nonzero_index([1, 2, 0, 0]) == 1
        assert m.last_nonzero_index([0, 0]) == -1
        assert m.last_nonzero_index([]) == -1
        assert m.last_nonzero_index([0, 0, 7]) == 2

    @staticmethod
    def evaluate(m):
        assert m.evaluate([3, 2, 5], 2) == 27
        assert m.evaluate([], 5) == 0
        assert m.evaluate([0, 0, 1], 3) == 9

    @staticmethod
    def pairs_with_gap(m):
        assert m.pairs_with_gap([1, 3, 5, 3], 2) == [(1, 3), (1, 3), (3, 5)]
        assert m.pairs_with_gap([1], 1) == []

    @staticmethod
    def total_by_key(m):
        assert m.total_by_key({"a": {"v": 1, "w": 2}, "b": {"v": 10}}) == {"a": 3, "b": 10}
        assert m.total_by_key({}) == {}

    @staticmethod
    def longest_name_id(m):
        assert m.longest_name_id({"7": {"name": "Ada"}, "12": {"name": "Margaret"}}) == "12"
        assert m.longest_name_id({"1": {"name": "ab"}, "2": {"name": "cd"}}) == "1"
        assert m.longest_name_id({}) is None

    @staticmethod
    def field_values(m):
        assert m.field_values({"10": {"t": 5}, "9": {"t": 7}, "11": {"t": 1}}, "t") == [7, 5, 1]

    @staticmethod
    def count_real_targets(m):
        data = {"1": {"TARGETS": {"a": {}, "b": {}, "longest": {}}}, "2": {"TARGETS": {"c": {}, "longest": {}}}}
        assert m.count_real_targets(data) == 3

    @staticmethod
    def minutes_of_type(m):
        data = {"1": {"TARGETS": {"a": {"type": "x", "minutes": 10}, "b": {"type": "y", "minutes": 5},
                                  "longest": {"name": "a", "minutes": 10}}},
                "2": {"TARGETS": {"c": {"type": "x", "minutes": 7}}}}
        assert m.minutes_of_type(data, "x") == 17
        assert m.minutes_of_type(data, "z") == 0

    @staticmethod
    def get_path(m):
        assert m.get_path({"a": {"b": 5}}, ["a", "b"]) == 5
        assert m.get_path({"a": {"b": 5}}, ["a", "c"]) is None
        assert m.get_path({"a": 1}, ["a", "b"]) is None
        assert m.get_path({"a": 1}, []) == {"a": 1}


# ---------------------------------------- ex2 ----------------------------------------
class Ex2:
    @staticmethod
    def average(m):
        assert m.average([1, 2, 6]) == 3.0
        assert m.average([]) is None

    @staticmethod
    def min_and_max(m):
        assert m.min_and_max([3, 9, 1]) == (1, 9)
        assert m.min_and_max([-5]) == (-5, -5)
        assert m.min_and_max([]) is None
        assert m.min_and_max([-3, -9]) == (-9, -3)

    @staticmethod
    def index_of_max(m):
        assert m.index_of_max([2, 9, 9, 1]) == 1
        assert m.index_of_max([]) == -1
        assert m.index_of_max([-5, -2]) == 1

    @staticmethod
    def longest_word(m):
        assert m.longest_word(["aa", "bbb", "ccc"]) == "bbb"
        assert m.longest_word([]) is None

    @staticmethod
    def count_by_first_letter(m):
        assert m.count_by_first_letter(["apple", "avocado", "kiwi", ""]) == {"a": 2, "k": 1}

    @staticmethod
    def average_by_group(m):
        assert m.average_by_group([("a", 1), ("b", 10), ("a", 3)]) == {"a": 2.0, "b": 10.0}
        assert m.average_by_group([]) == {}

    @staticmethod
    def group_by_length(m):
        assert m.group_by_length(["a", "bb", "c", "dd", "e"]) == {1: ["a", "c", "e"], 2: ["bb", "dd"]}

    @staticmethod
    def best_per_group(m):
        records = [{"name": "A", "g": 1, "v": 5}, {"name": "B", "g": 1, "v": 9}, {"name": "C", "g": 2, "v": 1}]
        assert m.best_per_group(records, "g", "v") == {1: "B", 2: "C"}

    @staticmethod
    def second_largest(m):
        assert m.second_largest([3, 9, 5, 9]) == 5
        assert m.second_largest([4, 4]) is None
        assert m.second_largest([]) is None
        assert m.second_largest([1, 2]) == 1
        assert m.second_largest([-1, -2, -3]) == -2

    @staticmethod
    def count_while(m):
        assert m.count_while([2, 4, 5, 6], lambda x: x % 2 == 0) == 2
        assert m.count_while([], lambda x: True) == 0
        assert m.count_while([1, 1], lambda x: True) == 2


# ---------------------------------------- ex3 ----------------------------------------
class Ex3:
    @staticmethod
    def sorted_unique(m):
        assert unchanged([3, 1, 3, 2], m.sorted_unique) == [1, 2, 3]

    @staticmethod
    def with_item(m):
        assert unchanged([1, 2], lambda l: m.with_item(l, 3)) == [1, 2, 3]

    @staticmethod
    def without_value(m):
        assert unchanged([1, 2, 1, 3], lambda l: m.without_value(l, 1)) == [2, 3]

    @staticmethod
    def add_in_place(m):
        l = [1]
        result = m.add_in_place(l, 2)
        assert result is None, "must return None"
        assert l == [1, 2], "the caller's list must be modified"

    @staticmethod
    def flatten_once(m):
        assert m.flatten_once([[1, 2], [3], [], [4, 5]]) == [1, 2, 3, 4, 5]

    @staticmethod
    def interleave(m):
        assert m.interleave([1, 2, 3], ["a"]) == [1, "a", 2, 3]
        assert m.interleave([], []) == []
        assert m.interleave([1], [2, 3]) == [1, 2, 3]

    @staticmethod
    def names_between(m):
        people = [{"name": "Zed", "year": 2000}, {"name": "Amy", "year": 2005}, {"name": "Bob", "year": 1990}]
        assert m.names_between(people, 2000, 2005) == ["Amy", "Zed"]
        assert m.names_between(people, 1800, 1801) == []

    @staticmethod
    def top_n(m):
        assert unchanged([4, 9, 1, 7], lambda l: m.top_n(l, 2)) == [9, 7]
        assert m.top_n([1, 2], 5) == [2, 1]

    @staticmethod
    def top_n_pairs(m):
        assert m.top_n_pairs([("a", 1), ("b", 5), ("c", 3)], 2) == [("b", 5), ("c", 3)]

    @staticmethod
    def normalize(m):
        assert unchanged([1, 2, 4], m.normalize) == [0.25, 0.5, 1.0]
        assert m.normalize([]) == []
        assert m.normalize([0, 0]) == [0, 0]

    @staticmethod
    def reverse_copy(m):
        assert unchanged([1, 2, 3], m.reverse_copy) == [3, 2, 1]

    @staticmethod
    def remove_negatives_in_place(m):
        l = [1, -2, -3, 3, -4]
        assert m.remove_negatives_in_place(l) is None
        assert l == [1, 3]

    @staticmethod
    def merge_dicts_sum(m):
        a, b = {"x": 1, "y": 2}, {"y": 5, "z": 1}
        assert m.merge_dicts_sum(a, b) == {"x": 1, "y": 7, "z": 1}
        assert a == {"x": 1, "y": 2} and b == {"y": 5, "z": 1}

    @staticmethod
    def swap_first_last(m):
        assert unchanged([1, 2, 3], m.swap_first_last) == [3, 2, 1]
        assert m.swap_first_last([]) == [] and m.swap_first_last([7]) == [7]


# ---------------------------------------- ex4 ----------------------------------------
class Ex4:
    @staticmethod
    def motzkin(m):
        assert [m.motzkin(n) for n in range(8)] == [1, 1, 2, 4, 9, 21, 51, 127]

    @staticmethod
    def motzkin_memo(m):
        assert [m.motzkin_memo(n) for n in range(8)] == [1, 1, 2, 4, 9, 21, 51, 127]
        assert m.motzkin_memo(30) == 1697385471211
        assert m.motzkin_memo(30) == 1697385471211, "second call in a row: is the cache handled correctly?"

    @staticmethod
    def motzkin_iter(m):
        assert [m.motzkin_iter(n) for n in range(8)] == [1, 1, 2, 4, 9, 21, 51, 127]
        assert m.motzkin_iter(30) == 1697385471211

    @staticmethod
    def delannoy_memo(m):
        assert m.delannoy_memo(1, 1) == 3
        assert m.delannoy_memo(2, 2) == 13
        assert m.delannoy_memo(3, 3) == 63
        assert m.delannoy_memo(3, 3) == 63         # twice in a row
        assert m.delannoy_memo(0, 5) == 1
        assert m.delannoy_memo(12, 12) == 251595969

    @staticmethod
    def binary_strings(m):
        assert m.binary_strings(0) == [""]
        assert m.binary_strings(2) == ["00", "01", "10", "11"]
        assert len(m.binary_strings(5)) == 32 and m.binary_strings(3)[5] == "101"

    @staticmethod
    def flatten(m):
        assert m.flatten([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]
        assert m.flatten([]) == [] and m.flatten([[], [[]]]) == []

    @staticmethod
    def digits_sum_rec(m):
        assert m.digits_sum_rec(4711) == 13 and m.digits_sum_rec(0) == 0

    @staticmethod
    def count_down(m):
        assert m.count_down(3) == [3, 2, 1, 0] and m.count_down(0) == [0]

    @staticmethod
    def palindromic(m):
        assert m.palindromic("kayak") and m.palindromic("") and not m.palindromic("ab")

    @staticmethod
    def _tree(m):
        N = m.Node
        return N(8, N(3, N(1), N(6, N(4), N(7))), N(10, None, N(14, N(13))))

    @staticmethod
    def collect_infix(m):
        assert m.collect_infix(None) == []
        assert m.collect_infix(Ex4._tree(m)) == [1, 3, 4, 6, 7, 8, 10, 13, 14]

    @staticmethod
    def collect_prefix(m):
        assert m.collect_prefix(Ex4._tree(m)) == [8, 3, 1, 6, 4, 7, 10, 14, 13]

    @staticmethod
    def leaf_values(m):
        assert m.leaf_values(Ex4._tree(m)) == [1, 4, 7, 13]
        assert m.leaf_values(None) == []

    @staticmethod
    def count_even(m):
        assert m.count_even(Ex4._tree(m)) == 5        # 8, 6, 4, 10, 14
        assert m.count_even(None) == 0

    @staticmethod
    def is_bst(m):
        N = m.Node
        assert m.is_bst(Ex4._tree(m)) is True
        assert m.is_bst(None) is True
        assert m.is_bst(N(5, N(3, None, N(6)), N(8))) is False      # 6 sits in the LEFT side of 5
        assert m.is_bst(N(5, N(5), None)) is False

    @staticmethod
    def depth_of_max(m):
        assert m.depth_of_max(Ex4._tree(m)) == 2
        assert m.depth_of_max(m.Node(1)) == 0


# ---------------------------------------- ex5 ----------------------------------------
class Ex5:
    @staticmethod
    def Stats(m):
        original = [3, 1, 2]
        s = m.Stats(original)
        original.append(99)
        assert s.values == [3, 1, 2], "the constructor must store a COPY"
        assert repr(s) == "Stats([3, 1, 2])" and len(s) == 3
        assert s.mean() == 2 and s.median() == 2
        assert m.Stats([1, 2, 3, 4]).median() == 2.5
        assert m.Stats([]).mean() is None and m.Stats([]).median() is None
        a, b = m.Stats([1, 2]), m.Stats([10])
        c = a + b
        assert c.values == [1, 2, 10] and a.values == [1, 2] and b.values == [10]
        assert a < b and not b < a
        d = a * 3
        assert d.values == [3, 6] and a.values == [1, 2]
        assert a.add(5) is None and a.values == [1, 2, 5]

    @staticmethod
    def Interval(m):
        a, b = m.Interval(1, 5), m.Interval(4, 10)
        assert repr(a) == "[1, 5]" and a.length() == 4
        assert a.contains(1) and a.contains(5) and not a.contains(6)
        assert a.overlaps(b) and b.overlaps(a) and not a.overlaps(m.Interval(6, 7))
        u = a + b
        assert (u.low, u.high) == (1, 10) and (a.low, a.high) == (1, 5)
        assert m.Interval(1, 2) == m.Interval(1, 2) and not a == b
        assert m.Interval(0, 1) < a and not a < m.Interval(0, 1)
        assert a.shift(2) is None and (a.low, a.high) == (3, 7)

    @staticmethod
    def Inventory(m):
        i, j = m.Inventory(), m.Inventory()
        i.add("nut", 10)
        i.add("bolt", 2)
        i.add("nut", 5)
        assert j.stock == {}, "each Inventory needs its OWN dict"
        assert i.quantity("nut") == 15 and i.quantity("zzz") == 0 and i.total() == 17
        i.remove("nut", 4)
        assert i.quantity("nut") == 11
        for bad in [("nut", 100), ("zzz", 1)]:
            try:
                i.remove(*bad)
            except ValueError:
                pass
            else:
                raise AssertionError("remove must raise ValueError")
        assert i.most_stocked() == "nut" and m.Inventory().most_stocked() is None
        assert i.low_stock(5) == ["bolt"] and i.low_stock(100) == ["bolt", "nut"]
        assert repr(i) == "Inventory(2 kinds, 13 items)"


# ---------------------------------------- ex6 ----------------------------------------
LIBRARY = {
    "b1": {"title": "Dune", "year": 1965, "authors": ["Herbert"], "copies": {"total": 5, "borrowed": 2},
           "tags": {"scifi": 9, "classic": 7, "longest": 0}},
    "b2": {"title": "Emma", "year": 1815, "authors": ["Austen"], "copies": {"total": 3, "borrowed": 3},
           "tags": {"classic": 8, "romance": 6, "longest": 0}},
    "b10": {"title": "Good Omens", "year": 1990, "authors": ["Pratchett", "Gaiman"],
            "copies": {"total": 4, "borrowed": 1}, "tags": {"scifi": 3, "fantasy": 8, "longest": 0}},
}
STUDENTS_CSV = """Name,Group,Grade,Age
Ana,A,15.5,19
Ben,B,12.0,21
Cleo,A,17.0,20
Dan,B,12.0,19
"""


class Ex6:
    @staticmethod
    def count_books(m):
        assert m.count_books(LIBRARY) == 3

    @staticmethod
    def available_copies(m):
        assert m.available_copies(LIBRARY, ["b1", "b2", "b10", "b99"]) == 3 + 0 + 3
        assert m.available_copies(LIBRARY, []) == 0

    @staticmethod
    def average_year(m):
        assert m.average_year(LIBRARY, ["b1", "b2", "zzz"]) == (1965 + 1815) / 2
        assert m.average_year(LIBRARY, ["zzz"]) is None

    @staticmethod
    def oldest_and_newest(m):
        assert m.oldest_and_newest(LIBRARY) == (("b2", 1815), ("b10", 1990))

    @staticmethod
    def count_by_author(m):
        assert m.count_by_author(LIBRARY) == {"Herbert": 1, "Austen": 1, "Pratchett": 1, "Gaiman": 1}

    @staticmethod
    def top_tags(m):
        result = m.top_tags(LIBRARY, 2)
        assert result["b1"] == [("scifi", 9), ("classic", 7)]
        assert result["b10"] == [("fantasy", 8), ("scifi", 3)]
        assert m.top_tags(LIBRARY, 5)["b2"] == [("classic", 8), ("romance", 6)]    # "longest" skipped

    @staticmethod
    def borrowed_by_decade(m):
        assert m.borrowed_by_decade(LIBRARY) == {1960: 2, 1810: 3, 1990: 1}

    @staticmethod
    def tag_totals(m):
        assert m.tag_totals(LIBRARY) == {"scifi": 12, "classic": 15, "romance": 6, "fantasy": 8}

    @staticmethod
    def ids_sorted_by_number(m):
        assert m.ids_sorted_by_number(LIBRARY) == ["b1", "b2", "b10"]

    @staticmethod
    def load_students(m):
        students = m.load_students(STUDENTS_CSV)
        assert len(students) == 4
        assert students[0] == {"Name": "Ana", "Group": "A", "Grade": 15.5, "Age": 19}
        assert isinstance(students[0]["Age"], int) and isinstance(students[0]["Grade"], float)

    @staticmethod
    def count_by_group(m):
        assert m.count_by_group(m.load_students(STUDENTS_CSV)) == {"A": 2, "B": 2}

    @staticmethod
    def best_student(m):
        assert m.best_student(m.load_students(STUDENTS_CSV)) == "Cleo"
        assert m.best_student([]) is None

    @staticmethod
    def average_grade_by_group(m):
        assert m.average_grade_by_group(m.load_students(STUDENTS_CSV)) == {"A": 16.25, "B": 12.0}

    @staticmethod
    def names_between_ages(m):
        students = m.load_students(STUDENTS_CSV)
        assert m.names_between_ages(students, 19, 20) == ["Ana", "Cleo", "Dan"]
        assert m.names_between_ages(students, 50, 60) == []

    @staticmethod
    def insertion_sort(m):
        students = m.load_students(STUDENTS_CSV)
        before = list(students)
        result = m.insertion_sort(students, key=lambda s: s["Grade"])
        assert students == before and result is not students, "must return a NEW list"
        assert [s["Name"] for s in result] == ["Ben", "Dan", "Ana", "Cleo"], "equal keys must keep their order (stable)"
        assert m.insertion_sort([], key=lambda x: x) == []
        assert m.insertion_sort([3, 1, 2], key=lambda x: -x) == [3, 2, 1]


CLASSES = {"ex1_keys_and_indices": Ex1, "ex2_accumulators": Ex2, "ex3_return_vs_mutate": Ex3,
           "ex4_recursion_memo": Ex4, "ex5_classes": Ex5, "ex6_json_csv": Ex6}


def run(selected, folder, verbose):
    passed = failed = todo = 0
    for module_name, checks in CLASSES.items():
        if selected and not any(module_name.startswith(s) for s in selected):
            continue
        print(f"\n=== {module_name}")
        module = load(module_name, folder)
        for name in [n for n in vars(checks) if not n.startswith("_")]:
            check = getattr(checks, name)
            try:
                check(module)
            except NotImplementedError:
                print(f"  TODO  {name}")
                todo += 1
            except Exception as error:               # AssertionError, TypeError, KeyError...
                failed += 1
                last = traceback.extract_tb(error.__traceback__)[-1]
                print(f"  FAIL  {name}: {type(error).__name__}: {error}   (line {last.lineno} of {os.path.basename(last.filename)})")
                if verbose:
                    traceback.print_exc()
            else:
                print(f"  OK    {name}")
                passed += 1
    print(f"\n{passed} OK, {failed} FAIL, {todo} TODO")
    return failed


if __name__ == "__main__":
    args = sys.argv[1:]
    verbose = "-v" in args
    use_solutions = "--solutions" in args
    selected = [a for a in args if not a.startswith("-")]
    folder = SOLUTIONS if use_solutions else HERE
    sys.exit(1 if run(selected, folder, verbose) else 0)
