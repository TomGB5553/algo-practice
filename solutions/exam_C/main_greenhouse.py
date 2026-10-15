# Exercise 3 : try your functions here
from src.greenhouse import *

data = load_data("data/greenhouse.json")
print(count_days(data))
print(get_avg_temp(data, [301, 302, 303]))
print(get_extreme_temp(data))
print(count_by_weather(data))
print(get_tallest_plants(data, 2)["301"])
print(get_meters_by_family(data))
print(days_with_plant(data, "basil"))
