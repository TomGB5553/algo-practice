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


def count_books(library):
    """Number of books."""
    raise NotImplementedError


def available_copies(library, book_ids):
    """Total number of copies NOT borrowed (total - borrowed) over the given list of ids (strings).
    Ids that are not in the library are ignored."""
    raise NotImplementedError


def average_year(library, book_ids):
    """Average publication year of the given ids (ignore unknown ones). None if no valid id."""
    raise NotImplementedError


def oldest_and_newest(library):
    """((id of the oldest book, its year), (id of the newest book, its year)). Ids stay strings."""
    raise NotImplementedError


def count_by_author(library):
    """{author: number of books}. `authors` is a LIST inside each book."""
    raise NotImplementedError


def top_tags(library, top_n=2):
    """{book id: [(tag, score), ...]} the top_n tags of each book by score (biggest first). Skip "longest"."""
    raise NotImplementedError


def borrowed_by_decade(library):
    """{decade: total borrowed copies}, decade = year // 10 * 10.  1965 -> 1960."""
    raise NotImplementedError


def tag_totals(library):
    """{tag: sum of its scores over all books} (skip "longest")."""
    raise NotImplementedError


def ids_sorted_by_number(library):
    """Ids sorted by their number: ["b10", "b2", "b1"] must give ["b1", "b2", "b10"] (not alphabetical!)."""
    raise NotImplementedError


def load_students(text):
    """List of dicts with Grade as float and Age as int; Name and Group stay strings."""
    raise NotImplementedError


def count_by_group(students):
    raise NotImplementedError


def best_student(students):
    """NAME of the student with the best grade, None if the list is empty."""
    raise NotImplementedError


def average_grade_by_group(students):
    raise NotImplementedError


def names_between_ages(students, youngest, oldest):
    """Sorted names of the students whose age is between the two values (both included). [] if none."""
    raise NotImplementedError


def insertion_sort(items, key):
    """Your own STABLE sort, returns a NEW list ascending by key(item), input untouched. No sorted() / .sort().
    Worst-case time complexity: O(n^2)  (write it as a comment in your answer)."""
    raise NotImplementedError
