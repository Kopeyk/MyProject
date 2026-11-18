"""Статистика за оцінками групи."""


def best_students(scores, limit=3):
    """Повертає імена студентів з найвищими балами."""
    ranked = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    return [name for name, _ in ranked[:limit]]
