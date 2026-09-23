"""Distance calculation utilities."""

from math import hypot
from typing import Sequence


def euclidean_distance(point_a: Sequence[float], point_b: Sequence[float]) -> float:
    """Return the Euclidean distance between two 2D points."""
    if len(point_a) != 2 or len(point_b) != 2:
        raise ValueError("Points must contain exactly two coordinates.")

    return hypot(point_a[0] - point_b[0], point_a[1] - point_b[1])
