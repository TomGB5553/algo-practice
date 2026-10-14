import pytest

# Small data set, easy to check by hand. Night keys are STRINGS.
DATA = {
    "10": {
        "SEEING": {"av": 2.0, "ct": 10, "mn": 1.0, "mx": 3.0},
        "TARGETS": {
            "A": {"type": "galaxy", "minutes": 30},
            "B": {"type": "nebula", "minutes": 90},
            "C": {"type": "galaxy", "minutes": 60},
            "D": {"type": "star", "minutes": 15},
            "longest": {"name": "B", "minutes": 90},
        },
        "Moon_phase": "full",
    },
    "11": {
        "SEEING": {"av": 3.0, "ct": 10, "mn": 0.5, "mx": 5.0},
        "TARGETS": {
            "E": {"type": "star", "minutes": 120},
            "longest": {"name": "E", "minutes": 120},
        },
        "Moon_phase": "new",
    },
    "15": {
        "SEEING": {"av": 4.0, "ct": 10, "mn": 2.0, "mx": 4.5},
        "TARGETS": {
            "F": {"type": "nebula", "minutes": 60},
            "G": {"type": "galaxy", "minutes": 45},
            "longest": {"name": "F", "minutes": 60},
        },
        "Moon_phase": "full",
    },
}


def test_load_data():
    from src.observatory import load_data
    from src.observatory_data import OBSERVATORY_DATA

    data = load_data("data/observatory.json")
    assert isinstance(data, dict)
    assert data == OBSERVATORY_DATA


def test_count_nights():
    from src.observatory import count_nights
    from src.observatory_data import OBSERVATORY_DATA

    assert count_nights(DATA) == 3
    assert count_nights(OBSERVATORY_DATA) == 27
    assert count_nights({}) == 0


def test_get_avg_seeing():
    from src.observatory import get_avg_seeing

    assert get_avg_seeing(DATA, [10, 11]) == pytest.approx(2.5)
    assert get_avg_seeing(DATA, [10, 11, 15]) == pytest.approx(3.0)
    # missing nights are ignored
    assert get_avg_seeing(DATA, [10, 12, 13, 15]) == pytest.approx(3.0)
    # no valid night -> None
    assert get_avg_seeing(DATA, [1, 2]) is None
    assert get_avg_seeing(DATA, []) is None


def test_get_extreme_seeing():
    from src.observatory import get_extreme_seeing

    (night_min, mn), (night_max, mx) = get_extreme_seeing(DATA)
    assert night_min == 11 and isinstance(night_min, int)
    assert mn == 0.5
    assert night_max == 11 and isinstance(night_max, int)
    assert mx == 5.0

    other = {"20": DATA["10"], "21": DATA["15"]}
    assert get_extreme_seeing(other) == ((20, 1.0), (21, 4.5))


def test_count_by_moon_phase():
    from src.observatory import count_by_moon_phase

    assert count_by_moon_phase(DATA) == {"full": 2, "new": 1}
    assert count_by_moon_phase({}) == {}


def test_get_top_targets():
    from src.observatory import get_top_targets

    top = get_top_targets(DATA)  # default top_n = 3
    assert top["10"] == [("B", 90), ("C", 60), ("A", 30)]
    assert top["11"] == [("E", 120)]  # fewer than 3 targets
    assert top["15"] == [("F", 60), ("G", 45)]
    assert "longest" not in str(top)

    assert get_top_targets(DATA, 1)["10"] == [("B", 90)]
    assert set(top.keys()) == {"10", "11", "15"}  # keys stay strings


def test_get_hours_by_type():
    from src.observatory import get_hours_by_type

    hours = get_hours_by_type(DATA)
    assert set(hours.keys()) == {"galaxy", "nebula", "star"}
    assert hours["galaxy"] == pytest.approx((30 + 60 + 45) / 60)
    assert hours["nebula"] == pytest.approx((90 + 60) / 60)
    assert hours["star"] == pytest.approx((15 + 120) / 60)


def test_on_real_data():
    from src.observatory import (
        count_by_moon_phase,
        get_avg_seeing,
        get_extreme_seeing,
        get_top_targets,
    )
    from src.observatory_data import OBSERVATORY_DATA as D

    assert get_avg_seeing(D, [101, 102, 107]) == pytest.approx(2.4755)
    assert get_extreme_seeing(D) == ((128, -0.295), (118, 4.524))
    assert count_by_moon_phase(D) == {"new": 7, "first quarter": 4, "last quarter": 9, "full": 7}
    assert get_top_targets(D, 2)["101"] == [("M42", 110), ("M57", 105)]
