import pytest

from myproject.calculator import average, grade


def test_average_of_list():
    assert average([60, 80, 100]) == 80


def test_average_of_empty_list():
    assert average([]) == 0.0


@pytest.mark.parametrize(
    "score, expected",
    [(95, "A"), (90, "A"), (85, "B"), (75, "C"), (70, "D"), (60, "E"), (59, "F"), (0, "F")],
)
def test_grade(score, expected):
    assert grade(score) == expected


@pytest.mark.parametrize("score", [-1, 101])
def test_grade_out_of_range(score):
    with pytest.raises(ValueError):
        grade(score)
