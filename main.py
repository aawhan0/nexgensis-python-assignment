"""Run the FastBox delivery simulation."""

import json

from loader import load_data
from simulation import simulate_delivery


def main() -> None:
    data = load_data("data.json")
    report = simulate_delivery(data)

    performers = [
        (agent_id, details)
        for agent_id, details in report.items()
        if details["packages_delivered"] > 0
    ]
    if performers:
        best_agent = min(
            performers,
            key=lambda item: (item[1]["efficiency"], item[0]),
        )[0]
    else:
        best_agent = None

    report["best_agent"] = best_agent

    with open("report.json", "w", encoding="utf-8") as file:
        json.dump(report, file, indent=2)

    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
