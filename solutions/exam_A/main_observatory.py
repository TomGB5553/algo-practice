from src.observatory import *

data = load_data("data/observatory.json")
print(count_nights(data))
print(get_avg_seeing(data, [101, 102, 107]))
print(get_extreme_seeing(data))
print(count_by_moon_phase(data))
print(get_top_targets(data, 2)["101"])
print(get_hours_by_type(data))
