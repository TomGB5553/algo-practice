"""
EX 6 : A FULL "JSON + CSV" MINI EXAM ON NEW DATA (a library)
   Same skills as exam A question 3 and exam B question 3, with another subject.
   Time yourself: 25 minutes for the whole file.

JSON `library` = {  "b1": {"title": "Dune", "year": 1965, "authors": ["Herbert"],
                           "copies": {"total": 5, "borrowed": 2},
                           "tags": {"scifi": 9, "classic": 7, "longest": 0}},      <- "longest" is NOT a tag: skip it
                    ... }       The keys are STRINGS "b1", "b2"... (some numbers may be missing)

CSV `students` text (use csv.DictReader on io.StringIO(text)) : columns Name,Group,Grade,Age
"""
import csv
import io


# ------------------------------- JSON -------------------------------

def count_books(library):
    """Number of books."""
    return len(library)


def available_copies(library, book_ids):
    """Total number of copies NOT borrowed (total - borrowed) over the given list of ids (strings).
    Ids that are not in the library are ignored."""
    total = 0
    for book_id in book_ids:
        if book_id in library:
            copies = library[book_id]["copies"]
            total += copies["total"] - copies["borrowed"]
    return total


def average_year(library, book_ids):
    """Average publication year of the given ids (ignore unknown ones). None if no valid id."""
    total = 0
    count = 0
    for book_id in book_ids:
        if book_id in library:
            total += library[book_id]["year"]
            count += 1
    if count == 0:
        return None
    return total / count


def oldest_and_newest(library):
    """((id of the oldest book, its year), (id of the newest book, its year)). Ids stay strings."""
    oldest = newest = None
    for book_id, book in library.items():
        if oldest is None or book["year"] < library[oldest]["year"]:
            oldest = book_id
        if newest is None or book["year"] > library[newest]["year"]:
            newest = book_id
    return (oldest, library[oldest]["year"]), (newest, library[newest]["year"])


def count_by_author(library):
    """{author: number of books}. `authors` is a LIST inside each book."""
    counts = {}
    for book in library.values():
        for author in book["authors"]:
            counts[author] = counts.get(author, 0) + 1
    return counts


def top_tags(library, top_n=2):
    """{book id: [(tag, score), ...]} the top_n tags of each book by score (biggest first). Skip "longest"."""
    result = {}
    for book_id, book in library.items():
        tags = []
        for tag, score in book["tags"].items():
            if tag == "longest":
                continue
            tags.append((tag, score))
        tags.sort(key=lambda t: t[1], reverse=True)
        result[book_id] = tags[:top_n]
    return result


def borrowed_by_decade(library):
    """{decade: total borrowed copies}, decade = year // 10 * 10.  1965 -> 1960."""
    result = {}
    for book in library.values():
        decade = book["year"] // 10 * 10
        result[decade] = result.get(decade, 0) + book["copies"]["borrowed"]
    return result


def tag_totals(library):
    """{tag: sum of its scores over all books} (skip "longest")."""
    totals = {}
    for book in library.values():
        for tag, score in book["tags"].items():
            if tag == "longest":
                continue
            totals[tag] = totals.get(tag, 0) + score
    return totals


def ids_sorted_by_number(library):
    """Ids sorted by their number: ["b10", "b2", "b1"] must give ["b1", "b2", "b10"] (not alphabetical!)."""
    return sorted(library, key=lambda book_id: int(book_id[1:]))


# ------------------------------- CSV -------------------------------

def load_students(text):
    """List of dicts with Grade as float and Age as int; Name and Group stay strings."""
    students = []
    for row in csv.DictReader(io.StringIO(text)):
        students.append({"Name": row["Name"], "Group": row["Group"],
                         "Grade": float(row["Grade"]), "Age": int(row["Age"])})
    return students


def count_by_group(students):
    counts = {}
    for s in students:
        counts[s["Group"]] = counts.get(s["Group"], 0) + 1
    return counts


def best_student(students):
    """NAME of the student with the best grade, None if the list is empty."""
    if len(students) == 0:
        return None
    best = students[0]
    for s in students:
        if s["Grade"] > best["Grade"]:
            best = s
    return best["Name"]


def average_grade_by_group(students):
    totals = {}
    counts = {}
    for s in students:
        g = s["Group"]
        totals[g] = totals.get(g, 0) + s["Grade"]
        counts[g] = counts.get(g, 0) + 1
    return {g: totals[g] / counts[g] for g in totals}


def names_between_ages(students, youngest, oldest):
    """Sorted names of the students whose age is between the two values (both included). [] if none."""
    return sorted(s["Name"] for s in students if youngest <= s["Age"] <= oldest)


def insertion_sort(items, key):
    """Your own STABLE sort, returns a NEW list ascending by key(item), input untouched. No sorted() / .sort().
    Worst-case time complexity: O(n^2)  (write it as a comment in your answer)."""
    result = []
    for item in items:
        position = len(result)
        while position > 0 and key(result[position - 1]) > key(item):
            position -= 1
        result.insert(position, item)
    return result
