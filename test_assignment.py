import math

from assignment import assign_packages
from distance import euclidean_distance
from loader import load_data
from simulation import simulate_delivery


def test_euclidean_distance() -> None:
    assert math.isclose(euclidean_distance([0, 0], [3, 4]), 5.0)


def test_load_assignment_data() -> None:
    data = load_data("data.json")
    assert set(data) == {"warehouses", "agents", "packages"}
    assert len(data["packages"]) == 5


def test_package_assignment() -> None:
    data = load_data("data.json")
    assignments = assign_packages(data)

    assert sum(len(packages) for packages in assignments.values()) == 5
    assert set(assignments) == set(data["agents"])


def test_delivery_simulation() -> None:
    data = load_data("data.json")
    report = simulate_delivery(data)

    assert sum(item["packages_delivered"] for item in report.values()) == 5
    assert all(item["total_distance"] >= 0 for item in report.values())
    assert all(item["efficiency"] >= 0 for item in report.values())


def test_alternate_json_input(tmp_path) -> None:
    import json

    alternate = {
        "warehouses": {"W1": [0, 0]},
        "agents": {"A1": [0, 0], "A2": [100, 100]},
        "packages": [
            {"id": "P1", "warehouse": "W1", "destination": [3, 4]},
        ],
    }
    path = tmp_path / "alternate.json"
    path.write_text(json.dumps(alternate), encoding="utf-8")

    data = load_data(str(path))
    report = simulate_delivery(data)

    assert report["A1"]["packages_delivered"] == 1
    assert report["A2"]["packages_delivered"] == 0
    assert report["A1"]["total_distance"] == 5.0
