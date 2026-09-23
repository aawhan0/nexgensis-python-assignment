from bonus import add_agent_mid_day, ascii_route, simulate_with_delays, write_top_performers_csv
from loader import load_data
from simulation import simulate_delivery


def test_optional_delay_and_route_features(tmp_path) -> None:
    data = load_data("data.json")
    report = simulate_delivery(data)

    delayed = simulate_with_delays(report, seed=42)
    assert all(
        details["total_delay_minutes"] >= 0
        for agent_id, details in delayed.items()
        if agent_id != "best_agent"
    )

    route = ascii_route(data, "A1", ["P1", "P4"])
    assert route == "A1 -> W1 -> P1 -> W1 -> P4"

    output = tmp_path / "top_performers.csv"
    write_top_performers_csv(report, str(output))
    assert output.exists()
    assert "A3" in output.read_text(encoding="utf-8")


def test_mid_day_agent_addition() -> None:
    data = load_data("data.json")
    updated = add_agent_mid_day(
        data,
        "A4",
        [50, 50],
        data["packages"][2:],
    )

    assert "A4" in updated["agents"]
    assert len(updated["packages"]) == 3
