import pytest

# Small data set, easy to check by hand. Day keys are STRINGS.
DATA = {
    "10": {
        "TEMP": {"av": 15.0, "ct": 10, "mn": 8.0, "mx": 22.0},
        "PLANTS": {
            "basil": {"family": "herb", "height_cm": 30},
            "rose": {"family": "flower", "height_cm": 90},
            "tomato": {"family": "vegetable", "height_cm": 120},
            "mint": {"family": "herb", "height_cm": 50},
            "tallest": {"name": "tomato", "height_cm": 120},
        },
        "Weather": "sunny",
    },
    "11": {
        "TEMP": {"av": 17.0, "ct": 10, "mn": 6.5, "mx": 25.0},
        "PLANTS": {
            "fern": {"family": "foliage", "height_cm": 40},
            "tallest": {"name": "fern", "height_cm": 40},
        },
        "Weather": "rainy",
    },
    "15": {
        "TEMP": {"av": 22.0, "ct": 10, "mn": 9.0, "mx": 30.5},
        "PLANTS": {
            "basil": {"family": "herb", "height_cm": 60},
            "tulip": {"family": "flower", "height_cm": 25},
            "tallest": {"name": "basil", "height_cm": 60},
        },
        "Weather": "sunny",
    },
}


def test_load_data():
    from src.greenhouse import load_data
    from src.greenhouse_data import GREENHOUSE_DATA

    data = load_data("data/greenhouse.json")
    assert isinstance(data, dict)
    assert data == GREENHOUSE_DATA


def test_count_days():
    from src.greenhouse import count_days
    from src.greenhouse_data import GREENHOUSE_DATA

    assert count_days(DATA) == 3
    assert count_days(GREENHOUSE_DATA) == 24
    assert count_days({}) == 0


def test_get_avg_temp():
    from src.greenhouse import get_avg_temp

    assert get_avg_temp(DATA, [10, 11]) == pytest.approx(16.0)
    assert get_avg_temp(DATA, [10, 11, 15]) == pytest.approx(18.0)
    # missing days are ignored (and not counted!)
    assert get_avg_temp(DATA, [10, 12, 13, 15]) == pytest.approx(18.5)
    assert get_avg_temp(DATA, [11]) == pytest.approx(17.0)


def test_get_avg_temp_none():
    from src.greenhouse import get_avg_temp

    assert get_avg_temp(DATA, [1, 2, 3]) is None
    assert get_avg_temp(DATA, []) is None
    assert get_avg_temp({}, [10]) is None


def test_get_extreme_temp():
    from src.greenhouse import get_extreme_temp

    result = get_extreme_temp(DATA)
    assert result == ((11, 6.5), (15, 30.5))
    (day_min, mn), (day_max, mx) = result
    assert isinstance(day_min, int) and isinstance(day_max, int)


def test_get_extreme_temp_real_data():
    from src.greenhouse import get_extreme_temp
    from src.greenhouse_data import GREENHOUSE_DATA

    assert get_extreme_temp(GREENHOUSE_DATA) == ((308, 4.0), (320, 32.6))


def test_get_extreme_temp_negative_values():
    from src.greenhouse import get_extreme_temp

    data = {
        "1": {"TEMP": {"av": -5.0, "ct": 1, "mn": -9.0, "mx": -2.0}},
        "2": {"TEMP": {"av": -6.0, "ct": 1, "mn": -4.0, "mx": -3.0}},
    }
    assert get_extreme_temp(data) == ((1, -9.0), (1, -2.0))


def test_count_by_weather():
    from src.greenhouse import count_by_weather
    from src.greenhouse_data import GREENHOUSE_DATA

    assert count_by_weather(DATA) == {"sunny": 2, "rainy": 1}
    counts = count_by_weather(GREENHOUSE_DATA)
    assert counts == {"windy": 4, "rainy": 10, "cloudy": 5, "sunny": 5}
    assert count_by_weather({}) == {}


def test_get_tallest_plants_default_top_2():
    from src.greenhouse import get_tallest_plants

    result = get_tallest_plants(DATA)
    assert result == {
        "10": [("tomato", 120), ("rose", 90)],
        "11": [("fern", 40)],
        "15": [("basil", 60), ("tulip", 25)],
    }


def test_get_tallest_plants_top_n():
    from src.greenhouse import get_tallest_plants

    result = get_tallest_plants(DATA, top_n=3)
    assert result["10"] == [("tomato", 120), ("rose", 90), ("mint", 50)]
    assert result["11"] == [("fern", 40)]
    assert get_tallest_plants(DATA, top_n=1)["10"] == [("tomato", 120)]
    # the key "tallest" is not a plant
    for plants in get_tallest_plants(DATA, top_n=10).values():
        assert "tallest" not in [name for name, _ in plants]


def test_get_tallest_plants_each_day_has_its_own_list():
    from src.greenhouse import get_tallest_plants

    result = get_tallest_plants(DATA, top_n=10)
    assert len(result["10"]) == 4
    assert len(result["11"]) == 1  # plants of day 10 must not leak into day 11
    assert len(result["15"]) == 2


def test_get_meters_by_family():
    from src.greenhouse import get_meters_by_family

    result = get_meters_by_family(DATA)
    assert set(result) == {"herb", "flower", "vegetable", "foliage"}
    assert result["herb"] == pytest.approx((30 + 50 + 60) / 100)
    assert result["flower"] == pytest.approx((90 + 25) / 100)
    assert result["vegetable"] == pytest.approx(1.2)
    assert result["foliage"] == pytest.approx(0.4)


def test_get_meters_by_family_real_data():
    from src.greenhouse import get_meters_by_family
    from src.greenhouse_data import GREENHOUSE_DATA

    result = get_meters_by_family(GREENHOUSE_DATA)
    assert result["herb"] == pytest.approx(18.12)
    assert result["vegetable"] == pytest.approx(20.52)
    assert result["succulent"] == pytest.approx(4.26)


def test_days_with_plant_bonus():
    from src.greenhouse import days_with_plant

    assert days_with_plant(DATA, "basil") == [10, 15]
    assert days_with_plant(DATA, "fern") == [11]
    assert days_with_plant(DATA, "orchid") == []
    assert days_with_plant({"9": DATA["10"], "10": DATA["10"], "100": DATA["15"]}, "basil") == [9, 10, 100]
    assert all(isinstance(d, int) for d in days_with_plant(DATA, "basil"))
