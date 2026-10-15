"""
JSON : LOAD, WALK AND QUERY A NESTED DICTIONARY   (the "observatory / insight" exercise)

Run:  python3 snippets/json_nested.py

=============================  HOW TO READ A NESTED DICT  =============================
Think in LAYERS. One `[...]` per layer:

    data["101"]["TARGETS"]["M42"]["minutes"]
          night   section   target   field        -> 110

RULES (the 5 errors that cost points in mock exam A)
 1. `for x in d`            gives the KEYS (strings), never the values.   d[x] is the value.
 2. `for k, v in d.items()` gives key AND value. Prefer it: v is already the inner dict.
 3. Before writing `[...]`, ask: "what TYPE do I hold?"
        night  (from `for night in data`)       -> str   : night["SEEING"]        is WRONG
        info   (from `.items()`)                -> dict  : info["SEEING"]["av"]   is OK
 4. JSON keys are ALWAYS strings: data[101] -> KeyError, data["101"] OK.  int("101") for the answer.
 5. Store each layer in a variable instead of one long chain.
 6. A key may be missing: `if key in d`, or `d.get(key, default)`.
 7. Some entries are NOT of the same kind (here "longest" inside TARGETS): skip them with `continue`.

JSON <-> Python : object {} = dict, array [] = list, string = str, number = int/float,
                  true/false = True/False, null = None.
"""
import json
import os
import tempfile

SAMPLE = {
    "101": {
        "SEEING": {"av": 2.958, "ct": 530, "mn": 2.046, "mx": 4.108},
        "TARGETS": {
            "M57": {"type": "nebula", "minutes": 105},
            "M42": {"type": "nebula", "minutes": 110},
            "M31": {"type": "galaxy", "minutes": 60},
            "longest": {"name": "M42", "minutes": 110},
        },
        "Moon_phase": "new",
        "Observer": "Ada",
    },
    "102": {
        "SEEING": {"av": 3.5, "ct": 400, "mn": 1.5, "mx": 5.0},
        "TARGETS": {
            "M13": {"type": "cluster", "minutes": 90},
            "M31": {"type": "galaxy", "minutes": 120},
            "longest": {"name": "M31", "minutes": 120},
        },
        "Moon_phase": "full",
        "Observer": "Bob",
    },
    "104": {                                   # night 103 is missing on purpose
        "SEEING": {"av": 2.0, "ct": 100, "mn": 1.0, "mx": 3.0},
        "TARGETS": {"M57": {"type": "nebula", "minutes": 30},
                    "longest": {"name": "M57", "minutes": 30}},
        "Moon_phase": "new",
        "Observer": "Ada",
    },
}


# ---------------------------------------------------------------------------------------------
# 1. LOAD / SAVE
# ---------------------------------------------------------------------------------------------
def load_data(file_path):
    with open(file_path) as file:          # `with` closes the file for you
        return json.load(file)             # json.load(file) for a FILE, json.loads(text) for a STRING


def save_data(data, file_path):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)


# ---------------------------------------------------------------------------------------------
# 2. COUNT
# ---------------------------------------------------------------------------------------------
def count_nights(data):
    return len(data)


def count_by_moon_phase(data):
    """{'new': 2, 'full': 1}   -> the COUNT IN A DICT pattern"""
    counts = {}
    for night, info in data.items():
        phase = info["Moon_phase"]
        counts[phase] = counts.get(phase, 0) + 1
    return counts


def count_by_observer(data):
    counts = {}
    for info in data.values():             # .values(): when the night number is not needed
        observer = info["Observer"]
        counts[observer] = counts.get(observer, 0) + 1
    return counts


# ---------------------------------------------------------------------------------------------
# 3. AVERAGE over a LIST OF KEYS, ignoring the missing ones  (None if nothing valid)
# ---------------------------------------------------------------------------------------------
def get_avg_seeing(data, nights):
    total = 0
    count = 0                              # BOTH start at 0 and BOTH are updated in the loop
    for night in nights:                   # nights is a list of INT
        key = str(night)                   # the keys are strings
        if key in data:                    # ignore the nights that are not in the data
            total += data[key]["SEEING"]["av"]
            count += 1
    if count == 0:                         # avoid dividing by zero
        return None
    return total / count


# ---------------------------------------------------------------------------------------------
# 4. MIN / MAX with the KEY that gives it  -> returns ((night_min, mn), (night_max, mx))
# ---------------------------------------------------------------------------------------------
def get_extreme_seeing(data):
    night_min = night_max = None
    lowest = highest = None
    for night, info in data.items():
        seeing = info["SEEING"]
        if lowest is None or seeing["mn"] < lowest:        # `is None or ...`: first element initialises
            lowest = seeing["mn"]
            night_min = int(night)                         # int() because the statement asks an integer
        if highest is None or seeing["mx"] > highest:      # note: > for the maximum
            highest = seeing["mx"]
            night_max = int(night)
    return (night_min, lowest), (night_max, highest)


# same with max(..., key=...) : shorter, but know the loop version too
def night_with_best_seeing(data):
    """Night (int) with the smallest average seeing."""
    best_key = min(data, key=lambda night: data[night]["SEEING"]["av"])   # min over the KEYS
    return int(best_key)


# ---------------------------------------------------------------------------------------------
# 5. A SUB-DICTIONARY INSIDE EACH ENTRY (skip the odd key)  + TOP N
# ---------------------------------------------------------------------------------------------
def get_top_targets(data, top_n=3):
    """{night: [(target, minutes), ...]} the top_n targets of each night, most minutes first."""
    result = {}
    for night, info in data.items():
        targets = []                                       # NEW list for each night (outside the inner loop)
        for name, target in info["TARGETS"].items():
            if name == "longest":
                continue                                   # skip this iteration only
            targets.append((name, target["minutes"]))      # ONE argument: a tuple
        targets.sort(key=lambda t: t[1], reverse=True)     # sort by minutes, biggest first
        result[night] = targets[:top_n]                    # slice = first top_n (also OK if fewer)
    return result


def get_hours_by_type(data):
    """{type: total hours over all the nights}  -> SUM IN A DICT pattern"""
    hours = {}
    for info in data.values():
        for name, target in info["TARGETS"].items():
            if name == "longest":
                continue
            kind = target["type"]
            hours[kind] = hours.get(kind, 0) + target["minutes"] / 60
    return hours


# ---------------------------------------------------------------------------------------------
# 6. FILTER : keep the entries that satisfy a condition (returns a list of keys / a sub-dict)
# ---------------------------------------------------------------------------------------------
def nights_with_target(data, target_name):
    result = []
    for night, info in data.items():
        if target_name in info["TARGETS"]:
            result.append(int(night))
    return sorted(result)                  # sorted(...) RETURNS the list; list.sort() returns None


def nights_by_observer(data, observer):
    return {night: info for night, info in data.items() if info["Observer"] == observer}


# ---------------------------------------------------------------------------------------------
# 7. FLATTEN a nested dict into a LIST OF OBJECTS / DICTS (like read_neos_from_json in the project)
# ---------------------------------------------------------------------------------------------
def flatten_targets(data):
    """[{'night': 101, 'target': 'M57', 'type': 'nebula', 'minutes': 105}, ...]"""
    rows = []
    for night, info in data.items():
        for name, target in info["TARGETS"].items():
            if name == "longest":
                continue
            rows.append({"night": int(night), "target": name,
                         "type": target["type"], "minutes": target["minutes"]})
    return rows


# ---------------------------------------------------------------------------------------------
# 8. SAFE ACCESS to a deep path (returns a default instead of crashing)
# ---------------------------------------------------------------------------------------------
def nested_get(data, keys, default=None):
    """nested_get(data, ['101', 'SEEING', 'av']) -> 2.958 ; missing key anywhere -> default"""
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current


# ---------------------------------------------------------------------------------------------
# 9. LIST OF DICTS  (JSON array of objects):  [{"name": "A", "age": 3}, ...]
# ---------------------------------------------------------------------------------------------
def oldest(people):
    """people = list of dicts. Return the NAME of the oldest (None if empty)."""
    best = None
    for person in people:
        if best is None or person["age"] > best["age"]:
            best = person
    return best["name"] if best is not None else None


def group_by(items, field):
    """{value of field: [items having it]}  -> GROUP IN A DICT pattern"""
    groups = {}
    for item in items:
        key = item[field]
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups


# ---------------------------------------------------------------------------------------------
# 10. SORT a dict by its values / its keys
# ---------------------------------------------------------------------------------------------
def ranking(counts):
    """[(key, value), ...] biggest value first;  ties broken by key (alphabetical)"""
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))


# ---------------------------------------------------------------------------------------------
if __name__ == "__main__":
    tmp = os.path.join(tempfile.mkdtemp(), "obs.json")
    save_data(SAMPLE, tmp)
    data = load_data(tmp)
    assert data == SAMPLE

    assert count_nights(data) == 3
    assert count_by_moon_phase(data) == {"new": 2, "full": 1}
    assert count_by_observer(data) == {"Ada": 2, "Bob": 1}

    assert get_avg_seeing(data, [101, 102]) == (2.958 + 3.5) / 2
    assert get_avg_seeing(data, [101, 103]) == 2.958          # 103 ignored
    assert get_avg_seeing(data, [999]) is None

    assert get_extreme_seeing(data) == ((104, 1.0), (102, 5.0))
    assert night_with_best_seeing(data) == 104

    top = get_top_targets(data, 2)
    assert top["101"] == [("M42", 110), ("M57", 105)]
    assert top["104"] == [("M57", 30)]

    hours = get_hours_by_type(data)
    assert abs(hours["nebula"] - (105 + 110 + 30) / 60) < 1e-9
    assert abs(hours["galaxy"] - (60 + 120) / 60) < 1e-9

    assert nights_with_target(data, "M31") == [101, 102]
    assert list(nights_by_observer(data, "Bob")) == ["102"]
    assert len(flatten_targets(data)) == 6
    assert nested_get(data, ["101", "SEEING", "av"]) == 2.958
    assert nested_get(data, ["103", "SEEING", "av"], "n/a") == "n/a"

    people = [{"name": "A", "age": 3}, {"name": "B", "age": 9}]
    assert oldest(people) == "B" and oldest([]) is None
    assert list(group_by(people, "age")) == [3, 9]
    assert ranking({"x": 2, "y": 5, "a": 2}) == [("y", 5), ("a", 2), ("x", 2)]

    print("json_nested: all OK")
