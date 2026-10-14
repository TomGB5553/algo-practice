import json


# 1 : json.load reads an open file and gives back a Python dict.
def load_data(file_path):
    with open(file_path, encoding="utf-8") as file:
        return json.load(file)


# 2 : len() of a dict = number of keys = number of nights.
def count_nights(data):
    return len(data)


# 3 : average of the "av" values of the SEEING of the requested nights.
# Keys of data are STRINGS, `nights` holds integers -> convert with str().
def get_avg_seeing(data, nights):
    total = 0
    count = 0
    for night in nights:
        key = str(night)
        if key in data:  # ignore the nights that do not exist
            total += data[key]["SEEING"]["av"]
            count += 1

    if count == 0:  # avoid dividing by 0
        return None
    return total / count


# 4 : lowest "mn" and highest "mx" of SEEING, with their night (as an int).
# We keep the best night seen so far and replace it when we find better.
def get_extreme_seeing(data):
    min_night = None
    min_value = None
    max_night = None
    max_value = None

    for key in data:
        seeing = data[key]["SEEING"]

        if min_value is None or seeing["mn"] < min_value:
            min_value = seeing["mn"]
            min_night = int(key)  # "101" -> 101

        if max_value is None or seeing["mx"] > max_value:
            max_value = seeing["mx"]
            max_night = int(key)

    return ((min_night, min_value), (max_night, max_value))


# 5 : counting with a dict: add 1 to the counter of each phase.
def count_by_moon_phase(data):
    counts = {}
    for key in data:
        phase = data[key]["Moon_phase"]
        if phase in counts:
            counts[phase] += 1
        else:
            counts[phase] = 1
    return counts


# 6 : for each night, the top_n targets by minutes.
def get_top_targets(data, top_n=3):
    result = {}
    for key in data:
        targets = []
        for name in data[key]["TARGETS"]:
            if name == "longest":  # a summary, not a target: skip it
                continue
            targets.append((name, data[key]["TARGETS"][name]["minutes"]))

        # sort on the 2nd element of the tuple (the minutes), biggest first
        targets.sort(key=lambda t: t[1], reverse=True)
        result[key] = targets[:top_n]  # slice: the first top_n elements
    return result


# 7 : total hours per type of target, over all the nights.
def get_hours_by_type(data):
    minutes_by_type = {}
    for key in data:
        for name in data[key]["TARGETS"]:
            if name == "longest":
                continue
            kind = data[key]["TARGETS"][name]["type"]
            minutes = data[key]["TARGETS"][name]["minutes"]
            minutes_by_type[kind] = minutes_by_type.get(kind, 0) + minutes

    # convert minutes to hours
    return {kind: minutes / 60 for kind, minutes in minutes_by_type.items()}
