"""Функції для обробки оцінок студентів."""


def average(values):
    """Повертає середнє арифметичне; для порожнього списку – 0.0."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def grade(score):
    """Переводить бал зі 100-бальної шкали в оцінку ECTS."""
    if score < 0 or score > 100:
        raise ValueError("score must be between 0 and 100")
    if score >= 90:
        return "A"
    if score >= 82:
        return "B"
    if score >= 74:
        return "C"
    if score >= 64:
        return "D"
    if score >= 60:
        return "E"
    return "F"
