"""Delivery simulation and reporting."""

from typing import Any

from assignment import assign_packages
from distance import euclidean_distance


def simulate_delivery(data: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """Simulate deliveries and return per-agent delivery statistics."""
    assignments = assign_packages(data)
    agents = data["agents"]
    warehouses = data["warehouses"]

    report: dict[str, dict[str, Any]] = {}

    for agent_id, packages in assignments.items():
        current_position = agents[agent_id]
        total_distance = 0.0

        for package in packages:
            warehouse = warehouses[package["warehouse"]]

            # An agent travels from its current position to the package warehouse.
            total_distance += euclidean_distance(current_position, warehouse)

            # After delivery, the agent remains at the package destination.
            total_distance += euclidean_distance(warehouse, package["destination"])
            current_position = package["destination"]

        delivered = len(packages)
        efficiency = total_distance / delivered if delivered else 0.0

        report[agent_id] = {
            "packages_delivered": delivered,
            "total_distance": round(total_distance, 2),
            "efficiency": round(efficiency, 2),
        }

    return report
