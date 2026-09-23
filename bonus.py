"""Optional enhancements for the FastBox simulator."""

import csv
import random
from copy import deepcopy
from typing import Any


def add_agent_mid_day(
    data: dict[str, Any],
    agent_id: str,
    position: list[float],
    remaining_packages: list[dict[str, Any]],
) -> dict[str, Any]:
    """Return a copy of the input with a new agent available for remaining packages."""
    updated = deepcopy(data)
    updated["agents"][agent_id] = position
    updated["packages"] = remaining_packages
    return updated


def simulate_with_delays(
    report: dict[str, dict[str, Any]],
    seed: int = 42,
    max_delay: int = 10,
) -> dict[str, dict[str, Any]]:
    """Add reproducible random delivery delays to a simulation report."""
    rng = random.Random(seed)
    delayed = deepcopy(report)

    for agent_id, details in delayed.items():
        if agent_id == "best_agent":
            continue
        packages = details["packages_delivered"]
        details["total_delay_minutes"] = sum(
            rng.randint(0, max_delay) for _ in range(packages)
        )

    return delayed


def ascii_route(
    data: dict[str, Any],
    agent_id: str,
    package_ids: list[str],
) -> str:
    """Render a compact textual route for an agent."""
    packages = {package["id"]: package for package in data["packages"]}
    route = [agent_id]

    for package_id in package_ids:
        package = packages[package_id]
        route.extend([package["warehouse"], package_id])

    return " -> ".join(route)


def write_top_performers_csv(
    report: dict[str, dict[str, Any]],
    output_path: str = "top_performers.csv",
) -> None:
    """Write agents ordered by average distance per delivered package."""
    rows = [
        {
            "agent_id": agent_id,
            "packages_delivered": details["packages_delivered"],
            "total_distance": details["total_distance"],
            "efficiency": details["efficiency"],
        }
        for agent_id, details in report.items()
        if agent_id != "best_agent"
    ]
    rows.sort(key=lambda row: (row["efficiency"], row["agent_id"]))

    with open(output_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "agent_id",
                "packages_delivered",
                "total_distance",
                "efficiency",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)
