import pytest

PLANETS = [
    {"Name": "A", "Year": 2000, "Distance_ly": 10.0, "Mass_earth": 5.0, "Method": "Transit"},
    {"Name": "B", "Year": 2005, "Distance_ly": 30.0, "Mass_earth": 50.0, "Method": "Imaging"},
    {"Name": "C", "Year": 2010, "Distance_ly": 20.0, "Mass_earth": 7.0, "Method": "Transit"},
    {"Name": "D", "Year": 2005, "Distance_ly": 50.0, "Mass_earth": 1.0, "Method": "Transit"},
]


def test_load_planets():
    from src.planets import load_planets

    planets = load_planets("data/exoplanets.csv")
    assert len(planets) == 40
    first = planets[0]
    assert first["Name"] == "Kepler-563d"
    assert first["Year"] == 2016 and isinstance(first["Year"], int)
    assert first["Distance_ly"] == 1026.5 and isinstance(first["Distance_ly"], float)
    assert first["Mass_earth"] == 57.1 and isinstance(first["Mass_earth"], float)
    assert first["Method"] == "Microlensing"


def test_count_by_method():
    from src.planets import count_by_method

    assert count_by_method(PLANETS) == {"Transit": 3, "Imaging": 1}
    assert count_by_method([]) == {}


def test_heaviest_planet():
    from src.planets import heaviest_planet

    assert heaviest_planet(PLANETS) == "B"
    assert isinstance(heaviest_planet(PLANETS), str)
    assert heaviest_planet([]) is None


def test_average_distance_by_method():
    from src.planets import average_distance_by_method

    result = average_distance_by_method(PLANETS)
    assert result["Transit"] == pytest.approx((10 + 20 + 50) / 3)
    assert result["Imaging"] == pytest.approx(30.0)


def test_planets_between():
    from src.planets import planets_between

    assert planets_between(PLANETS, 2005, 2010) == ["B", "C", "D"]
    assert planets_between(PLANETS, 2001, 2004) == []
    assert planets_between(PLANETS, 2000, 2000) == ["A"]


def test_insertion_sort():
    from src.planets import insertion_sort
    from tests.code_checks import called_names

    before = list(PLANETS)
    result = insertion_sort(PLANETS, key=lambda p: p["Year"])
    assert [p["Name"] for p in result] == ["A", "B", "D", "C"]  # B before D: stable
    assert PLANETS == before, "the input list must not be modified"
    assert result is not PLANETS

    by_mass = insertion_sort(PLANETS, key=lambda p: p["Mass_earth"])
    assert [p["Name"] for p in by_mass] == ["D", "A", "C", "B"]
    assert insertion_sort([], key=lambda p: p) == []

    names = called_names(insertion_sort)
    assert "sorted" not in names and "sort" not in names, "write your own sort"
