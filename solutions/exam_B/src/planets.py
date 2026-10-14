import csv


# 1 : DictReader gives dicts of STRINGS; we convert the numeric columns.
def load_planets(path):
    planets = []
    with open(path, newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            planets.append({
                "Name": row["Name"],
                "Year": int(row["Year"]),
                "Distance_ly": float(row["Distance_ly"]),
                "Mass_earth": float(row["Mass_earth"]),
                "Method": row["Method"],
            })
    return planets


# 2 : counting with a dict.
def count_by_method(planets):
    counts = {}
    for planet in planets:
        method = planet["Method"]
        counts[method] = counts.get(method, 0) + 1  # .get(key, default)
    return counts


# 3 : "find the maximum" loop. Return the NAME, not the whole dict.
def heaviest_planet(planets):
    if len(planets) == 0:
        return None

    best = planets[0]
    for planet in planets:
        if planet["Mass_earth"] > best["Mass_earth"]:
            best = planet
    return best["Name"]


# 4 : average = sum / count, per method -> two dicts (sums and counts).
def average_distance_by_method(planets):
    sums = {}
    counts = {}
    for planet in planets:
        method = planet["Method"]
        sums[method] = sums.get(method, 0) + planet["Distance_ly"]
        counts[method] = counts.get(method, 0) + 1

    return {method: sums[method] / counts[method] for method in sums}


# 5 : filter then sort the names.
def planets_between(planets, first_year, last_year):
    names = []
    for planet in planets:
        if first_year <= planet["Year"] <= last_year:  # chained comparison
            names.append(planet["Name"])
    names.sort()  # alphabetical order, in place
    return names


# 6 : insertion sort.
# Complexity: worst case O(n^2) (reverse sorted input: each item must be
# moved past all the previous ones); best case O(n) (already sorted).
# Stable: we stop moving left as soon as the previous item is NOT strictly
# bigger, so equal items never cross.
def insertion_sort(planets, key):
    result = []  # the sorted part; the input list is never touched

    for planet in planets:
        result.append(planet)  # put it at the end...
        i = len(result) - 1
        # ...then move it to the left while the item before it is bigger
        while i > 0 and key(result[i - 1]) > key(result[i]):
            result[i - 1], result[i] = result[i], result[i - 1]
            i -= 1

    return result
