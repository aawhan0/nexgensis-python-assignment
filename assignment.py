"""Package assignment logic."""

from typing import Any

from distance import euclidean_distance


def assign_packages(data: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    """Assign each package to the nearest agent by warehouse distance.

    Ties are resolved deterministically by agent ID.
    """
    warehouses = data["warehouses"]
    agents = data["agents"]
    assignments = {agent_id: [] for agent_id in agents}

    for package in data["packages"]:
        warehouse = warehouses[package["warehouse"]]
        nearest_agent = min(
            agents,
            key=lambda agent_id: (
                euclidean_distance(agents[agent_id], warehouse),
                agent_id,
            ),
        )
        assignments[nearest_agent].append(package)

    return assignments
