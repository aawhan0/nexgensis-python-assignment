# Nexgensis Python Assignment

A small Python logistics simulator for the FastBox delivery scenario.

## Approach

1. Load and validate the JSON input.
2. Calculate Euclidean distance between 2D coordinates.
3. Assign each package to the nearest agent based on the agent's distance to the package warehouse.
4. Simulate each agent collecting its assigned packages and delivering them.
5. Calculate packages delivered, total distance, and average distance per package.
6. Save the final report to `report.json`.

## Project Structure

```text
.
├── assignment.py
├── data.json
├── distance.py
├── loader.py
├── main.py
├── report.json
├── simulation.py
└── test_assignment.py
```

## Run

Requires Python 3.10+.

```bash
python main.py
```

The program prints the report and writes it to `report.json`.

To run the tests:

```bash
python -m pytest test_assignment.py
```

## Assumptions

- Package assignment uses the Euclidean distance from the agent's current starting position to the package's warehouse, as specified by the assignment.
- If two agents are equally close to a warehouse, the agent ID is used as a deterministic tie-breaker.
- Packages assigned to an agent are processed in the same order they appear in `data.json`.
- After delivering a package, the agent's position becomes that package's destination.
- For each package, the agent travels from its current position to the package warehouse and then from the warehouse to the destination.
- The agent does not return to a warehouse after completing a delivery unless its next assigned package requires it.
- Efficiency is total distance divided by the number of packages delivered. Agents with no deliveries have an efficiency of 0.
- The assignment's sample report is treated as an example output format; the simulator calculates values from the stated routing logic rather than hard-coding those values.

## Validation

The included tests cover JSON loading, Euclidean distance, package assignment, package-count consistency, and non-negative delivery metrics.
