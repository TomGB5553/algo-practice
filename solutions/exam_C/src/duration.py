# Exercise 1 : the class Duration, and Playlist


class Duration:
    # Q1
    def __init__(self, hours, minutes):
        total = hours * 60 + minutes          # normalise: Duration(1, 75) is 2 h 15
        self.hours = total // 60
        self.minutes = total % 60

    # Q2
    def total_minutes(self):
        return self.hours * 60 + self.minutes

    # Q3
    def __repr__(self):
        return f"{self.hours}h{self.minutes:02d}"     # :02d pads with a zero: 5 -> "05"

    # Q4
    def __add__(self, other):
        return Duration(0, self.total_minutes() + other.total_minutes())

    def __lt__(self, other):
        return self.total_minutes() < other.total_minutes()   # method CALLED on each object, no argument

    # Q5
    def __mul__(self, k):
        return Duration(0, self.total_minutes() * k)


# Q6
class Playlist:
    def __init__(self, durations):
        self.durations = list(durations)      # a COPY

    def total(self):
        result = Duration(0, 0)
        for d in self.durations:
            result = result + d
        return result

    def longest(self):
        best = None
        for d in self.durations:
            if best is None or best < d:      # uses Duration.__lt__
                best = d
        return best
