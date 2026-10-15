"""
CSV : LOAD AND QUERY A TABLE   (the "exoplanets / flights" exercise)

Run:  python3 snippets/csv_data.py

=============================  CSV RULES  =============================
 1. EVERYTHING is read as a STRING -> convert: int(row["Year"]), float(row["Mass"]).
 2. Open with  open(path, newline="")  and use  csv.DictReader(file)  -> each row is a dict {column: str}.
 3. The column names are the first line of the file: spell them EXACTLY (case matters).
 4. A cell can be empty (""): int("") crashes -> test `if row["Mass"] != ""` when the statement warns you.
 5. Result of a function = list of dicts (keep it simple), then every question is a loop over that list.
 6. Writing: csv.DictWriter(file, fieldnames=[...]) + writeheader() + writerow(d).

Patterns below use `planets` = list of dicts like
    {"Name": "Kepler-563d", "Year": 2016, "Distance_ly": 1026.5, "Mass_earth": 57.1, "Method": "Transit"}
"""
import csv
import io
import os
import tempfile

SAMPLE_CSV = """Name,Year,Distance_ly,Mass_earth,Method
Kepler-563d,2016,1026.5,57.1,Microlensing
Ross-530c,2008,883.0,198.3,Microlensing
HD-11d,2012,1755.4,78.4,Microlensing
Luyten-872e,2005,33.3,454.4,Transit
Gliese-9b,2012,12.0,3.2,Transit
Tau-7c,2016,300.0,198.3,Transit
"""


# ---------------------------------------------------------------------------------------------
# 1. LOAD (with conversions)
# ---------------------------------------------------------------------------------------------
def load_planets(path):
    planets = []
    with open(path, newline="") as file:
        for row in csv.DictReader(file):
            planets.append({                       # .append  (not .apend !)
                "Name": row["Name"],
                "Year": int(row["Year"]),
                "Distance_ly": float(row["Distance_ly"]),
                "Mass_earth": float(row["Mass_earth"]),
                "Method": row["Method"],
            })
    return planets


def load_generic(path):
    """Plain strings, no conversion: [{'col': 'value', ...}, ...]"""
    with open(path, newline="") as file:
        return list(csv.DictReader(file))


def load_columns(path):
    """Without DictReader: csv.reader gives LISTS, row[0] is the first column (header included)."""
    with open(path, newline="") as file:
        rows = list(csv.reader(file))
    header, body = rows[0], rows[1:]
    return header, body


# ---------------------------------------------------------------------------------------------
# 2. COUNT / GROUP / AVERAGE BY CATEGORY
# ---------------------------------------------------------------------------------------------
def count_by_method(planets):
    counts = {}
    for planet in planets:
        method = planet["Method"]                      # the KEY is the category, NOT the whole planet
        counts[method] = counts.get(method, 0) + 1
    return counts


def average_distance_by_method(planets):
    sums = {}
    counts = {}
    for planet in planets:
        method = planet["Method"]
        sums[method] = sums.get(method, 0) + planet["Distance_ly"]
        counts[method] = counts.get(method, 0) + 1     # counts += 1, NOT sums...
    return {method: sums[method] / counts[method] for method in sums}


def group_names_by_method(planets):
    groups = {}
    for planet in planets:
        method = planet["Method"]
        if method not in groups:
            groups[method] = []
        groups[method].append(planet["Name"])
    return groups


# ---------------------------------------------------------------------------------------------
# 3. FIND THE BEST (return the NAME, or None if empty)
# ---------------------------------------------------------------------------------------------
def heaviest_planet(planets):
    if len(planets) == 0:                              # empty case first
        return None
    best = planets[0]
    for planet in planets:
        if planet["Mass_earth"] > best["Mass_earth"]:
            best = planet
    return best["Name"]                                # the statement asked for the NAME


def closest_per_method(planets):
    """{method: name of its closest planet}  -> best-per-category pattern"""
    best = {}
    for planet in planets:
        method = planet["Method"]
        if method not in best or planet["Distance_ly"] < best[method]["Distance_ly"]:
            best[method] = planet
    return {method: p["Name"] for method, p in best.items()}


# ---------------------------------------------------------------------------------------------
# 4. FILTER + SORT  (sorted() RETURNS a list; list.sort() returns None -> never `return l.sort()`)
# ---------------------------------------------------------------------------------------------
def planets_between(planets, first_year, last_year):
    names = []
    for planet in planets:
        if first_year <= planet["Year"] <= last_year:  # chained comparison, both included
            names.append(planet["Name"])
    return sorted(names)                               # empty list if nothing (NOT None)


def top_n_heaviest(planets, n=3):
    """The n heaviest planets (dicts), heaviest first."""
    return sorted(planets, key=lambda p: p["Mass_earth"], reverse=True)[:n]


def sort_by_two_criteria(planets):
    """By Year ascending, then by Name. Trick: key returns a TUPLE."""
    return sorted(planets, key=lambda p: (p["Year"], p["Name"]))


def sort_year_desc_name_asc(planets):
    """Mixed directions: negate the numeric key."""
    return sorted(planets, key=lambda p: (-p["Year"], p["Name"]))


# ---------------------------------------------------------------------------------------------
# 5. YOUR OWN SORT (when `sorted` is forbidden): INSERTION SORT, STABLE, returns a NEW list
#    time O(n^2) worst case (reverse-sorted input), O(n) if already sorted
# ---------------------------------------------------------------------------------------------
def insertion_sort(items, key):
    result = []
    for item in items:                                 # take the items one by one, in original order
        position = len(result)
        # move left while the element on the left is STRICTLY bigger (strict > keeps equal items in order)
        while position > 0 and key(result[position - 1]) > key(item):
            position -= 1
        result.insert(position, item)
    return result


def selection_sort(items, key):
    """time O(n^2) always. Not stable in the classic swap version; this version is (it pops the first minimum)."""
    remaining = list(items)                            # copy: do not modify the input
    result = []
    while remaining:
        best_index = 0
        for i in range(1, len(remaining)):
            if key(remaining[i]) < key(remaining[best_index]):   # strict < : first minimum wins
                best_index = i
        result.append(remaining.pop(best_index))
    return result


def bubble_sort(numbers):
    """In-place on a COPY. time O(n^2), O(n) if already sorted (with the `swapped` flag)."""
    l = list(numbers)
    for end in range(len(l) - 1, 0, -1):
        swapped = False
        for i in range(end):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                swapped = True
        if not swapped:
            break
    return l


# ---------------------------------------------------------------------------------------------
# 6. STATISTICS
# ---------------------------------------------------------------------------------------------
def mean(values):
    if len(values) == 0:
        return None
    return sum(values) / len(values)


def median(values):
    if len(values) == 0:
        return None
    s = sorted(values)
    middle = len(s) // 2
    if len(s) % 2 == 1:
        return s[middle]
    return (s[middle - 1] + s[middle]) / 2


def most_common(values):
    counts = {}
    for v in values:
        counts[v] = counts.get(v, 0) + 1
    best = None
    for v, c in counts.items():
        if best is None or c > counts[best]:
            best = v
    return best


# ---------------------------------------------------------------------------------------------
# 7. WRITE A CSV
# ---------------------------------------------------------------------------------------------
def save_planets(planets, path):
    with open(path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Year", "Distance_ly", "Mass_earth", "Method"])
        writer.writeheader()
        for planet in planets:
            writer.writerow(planet)


# ---------------------------------------------------------------------------------------------
# 8. NO FILE : parse CSV text already in memory (handy for tests)
# ---------------------------------------------------------------------------------------------
def parse_text(text):
    return list(csv.DictReader(io.StringIO(text)))


# ---------------------------------------------------------------------------------------------
if __name__ == "__main__":
    path = os.path.join(tempfile.mkdtemp(), "planets.csv")
    with open(path, "w", newline="") as f:
        f.write(SAMPLE_CSV)

    planets = load_planets(path)
    assert len(planets) == 6 and planets[0]["Year"] == 2016 and planets[0]["Mass_earth"] == 57.1
    assert load_generic(path)[0]["Year"] == "2016"                  # string without conversion
    assert load_columns(path)[0][0] == "Name"

    assert count_by_method(planets) == {"Microlensing": 3, "Transit": 3}
    assert average_distance_by_method(planets)["Transit"] == (33.3 + 12.0 + 300.0) / 3
    assert group_names_by_method(planets)["Transit"] == ["Luyten-872e", "Gliese-9b", "Tau-7c"]

    assert heaviest_planet(planets) == "Luyten-872e" and heaviest_planet([]) is None
    assert closest_per_method(planets) == {"Microlensing": "Ross-530c", "Transit": "Gliese-9b"}

    assert planets_between(planets, 2012, 2016) == ["Gliese-9b", "HD-11d", "Kepler-563d", "Tau-7c"]
    assert planets_between(planets, 1900, 1901) == []
    assert [p["Name"] for p in top_n_heaviest(planets, 2)] == ["Luyten-872e", "Ross-530c"]
    assert [p["Name"] for p in sort_by_two_criteria(planets)][:2] == ["Luyten-872e", "Ross-530c"]
    assert [p["Name"] for p in sort_year_desc_name_asc(planets)][:2] == ["Kepler-563d", "Tau-7c"]

    # insertion sort: new list, input untouched, stable (Ross-530c and Tau-7c share the mass 198.3)
    original = list(planets)
    by_mass = insertion_sort(planets, key=lambda p: p["Mass_earth"])
    assert planets == original and by_mass is not planets
    assert [p["Name"] for p in by_mass] == ["Gliese-9b", "Kepler-563d", "HD-11d", "Ross-530c", "Tau-7c", "Luyten-872e"]
    assert selection_sort(planets, key=lambda p: p["Mass_earth"]) == by_mass
    assert bubble_sort([5, 1, 4, 2]) == [1, 2, 4, 5]

    assert mean([1, 2, 3]) == 2 and mean([]) is None
    assert median([5, 1, 3]) == 3 and median([1, 2, 3, 4]) == 2.5
    assert most_common(["a", "b", "a"]) == "a"

    out = os.path.join(os.path.dirname(path), "out.csv")
    save_planets(planets, out)
    assert len(load_generic(out)) == 6
    assert parse_text("a,b\n1,2\n")[0] == {"a": "1", "b": "2"}

    print("csv_data: all OK")
