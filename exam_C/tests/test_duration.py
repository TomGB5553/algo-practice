import pytest


def test_constructor_and_normalisation():
    from src.duration import Duration

    d = Duration(2, 30)
    assert (d.hours, d.minutes) == (2, 30)
    e = Duration(1, 75)  # 75 minutes = 1 h 15 more
    assert (e.hours, e.minutes) == (2, 15)
    f = Duration(0, 60)
    assert (f.hours, f.minutes) == (1, 0)


def test_total_minutes():
    from src.duration import Duration

    assert Duration(2, 30).total_minutes() == 150
    assert Duration(0, 0).total_minutes() == 0
    assert Duration(1, 75).total_minutes() == 135


def test_repr():
    from src.duration import Duration

    assert repr(Duration(2, 15)) == "2h15"
    assert repr(Duration(0, 5)) == "0h05"
    assert str(Duration(1, 0)) == "1h00"


def test_add_returns_new_duration():
    from src.duration import Duration

    a = Duration(1, 45)
    b = Duration(0, 50)
    c = a + b
    assert isinstance(c, Duration)
    assert (c.hours, c.minutes) == (2, 35)
    assert (a.hours, a.minutes) == (1, 45)
    assert (b.hours, b.minutes) == (0, 50)
    assert c is not a and c is not b


def test_lt():
    from src.duration import Duration

    assert (Duration(0, 50) < Duration(1, 0)) is True
    assert (Duration(1, 0) < Duration(0, 50)) is False
    assert (Duration(1, 0) < Duration(0, 60)) is False  # equal: not strictly shorter
    assert (Duration(0, 130) < Duration(2, 11)) is True  # 130 min < 131 min


def test_mul():
    from src.duration import Duration

    a = Duration(1, 45)
    b = a * 3
    assert isinstance(b, Duration)
    assert (b.hours, b.minutes) == (5, 15)
    assert (a.hours, a.minutes) == (1, 45)
    assert (Duration(0, 20) * 0).total_minutes() == 0


def test_playlist_stores_a_copy():
    from src.duration import Duration, Playlist

    items = [Duration(0, 30), Duration(1, 0)]
    p = Playlist(items)
    items.append(Duration(5, 0))
    assert len(p.durations) == 2, "Playlist must store a COPY of the list"
    assert p.durations is not items


def test_playlist_total():
    from src.duration import Duration, Playlist

    items = [Duration(0, 40), Duration(0, 45), Duration(1, 5)]
    p = Playlist(items)
    total = p.total()
    assert isinstance(total, Duration)
    assert (total.hours, total.minutes) == (2, 30)
    assert [d.total_minutes() for d in items] == [40, 45, 65]  # items untouched
    empty = Playlist([]).total()
    assert isinstance(empty, Duration) and empty.total_minutes() == 0


def test_playlist_longest():
    from src.duration import Duration, Playlist

    longest = Playlist([Duration(0, 40), Duration(1, 5), Duration(0, 45)]).longest()
    assert longest.total_minutes() == 65
    assert Playlist([]).longest() is None


def test_main_duration(capsys):
    import runpy

    runpy.run_path("main_duration.py")
    lines = capsys.readouterr().out.strip().splitlines()
    assert lines == ["2h35", "0h50", "5h15"]
