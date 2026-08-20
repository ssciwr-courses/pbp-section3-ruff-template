from pathlib import Path

import pytest

from sensor_report import read_observations, render_report, summarize

FIXTURE = Path(__file__).parents[1] / "data" / "readings.csv"


def test_summarize_bundled_observations() -> None:
    summary = summarize(read_observations(FIXTURE))

    assert summary["samples"] == 4
    assert summary["sensors"] == 2
    assert summary["minimum_c"] == pytest.approx(21.8)
    assert summary["mean_c"] == pytest.approx(22.25)
    assert summary["maximum_c"] == pytest.approx(22.7)


def test_render_report() -> None:
    summary: dict[str, str | int | float] = {
        "samples": 4,
        "sensors": 2,
        "minimum_c": 21.8,
        "mean_c": 22.25,
        "maximum_c": 22.7,
    }

    assert render_report(summary) == (
        "4 readings from 2 sensors: mean 22.2 °C (range 21.8–22.7 °C)"
    )
