from myproject.statistics import best_students


def test_best_students_sorted_by_score():
    scores = {"Olena": 95, "Ivan": 70, "Petro": 88, "Anna": 91}
    assert best_students(scores, limit=2) == ["Olena", "Anna"]


def test_best_students_default_limit():
    scores = {"A": 1, "B": 2, "C": 3, "D": 4}
    assert best_students(scores) == ["D", "C", "B"]
