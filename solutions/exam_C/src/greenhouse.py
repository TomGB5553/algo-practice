# Exercise 3 : greenhouse JSON
import json


def load_data(file_path):
    with open(file_path) as file:
        return json.load(file)


def count_days(data):
    return len(data)


def get_avg_temp(data, days):
    total = 0
    count = 0
    for day in days:
        key = str(day)                      # keys are strings
        if key in data:
            total += data[key]["TEMP"]["av"]
            count += 1
    if count == 0:
        return None
    return total / count


def get_extreme_temp(data):
    day_min = day_max = None
    lowest = highest = None
    for day, info in data.items():          # .items(): `info` is the inner dict
        if lowest is None or info["TEMP"]["mn"] < lowest:
            lowest = info["TEMP"]["mn"]
            day_min = int(day)
        if highest is None or info["TEMP"]["mx"] > highest:
            highest = info["TEMP"]["mx"]
            day_max = int(day)
    return (day_min, lowest), (day_max, highest)


def count_by_weather(data):
    counts = {}
    for info in data.values():
        weather = info["Weather"]
        counts[weather] = counts.get(weather, 0) + 1
    return counts


def get_tallest_plants(data, top_n=2):
    result = {}
    for day, info in data.items():
        plants = []                         # a NEW list for each day
        for name, plant in info["PLANTS"].items():
            if name == "tallest":
                continue
            plants.append((name, plant["height_cm"]))
        plants.sort(key=lambda p: p[1], reverse=True)
        result[day] = plants[:top_n]
    return result


def get_meters_by_family(data):
    result = {}
    for info in data.values():
        for name, plant in info["PLANTS"].items():
            if name == "tallest":
                continue
            family = plant["family"]
            result[family] = result.get(family, 0) + plant["height_cm"] / 100
    return result


def days_with_plant(data, plant_name):
    days = []
    for day, info in data.items():
        if plant_name in info["PLANTS"] and plant_name != "tallest":
            days.append(int(day))
    return sorted(days)
