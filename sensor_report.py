"""Summarize temperature readings exported by laboratory sensors."""

import csv, json
import statistics
from pathlib import Path
import os

DATA_FILE=Path(__file__).parent / "data" / "readings.csv"



def read_observations(path:Path=DATA_FILE)->list[dict[str,str]]:
    """Read sensor observations from a CSV file."""
    with path.open(encoding="utf-8",newline="") as stream:
        return list(csv.DictReader(stream))


def summarize(observations:list[dict[str,str]])->dict[str,str|int|float]:
    """Calculate a compact summary of a non-empty observation sequence."""
    temperatures=[float(row["temperature_c"]) for row in observations]
    sensors={row["sensor"] for row in observations}
    return {"samples":len(temperatures),"sensors":len(sensors),"minimum_c":min(temperatures),"mean_c":statistics.fmean(temperatures),"maximum_c":max(temperatures)}


def render_report(summary:dict[str,str|int|float])->str:
    """Turn summary values into a report suitable for a terminal."""
    return (f"{summary['samples']} readings from {summary['sensors']} sensors: "
    f"mean {summary['mean_c']:.1f} °C "
    f"(range {summary['minimum_c']:.1f}–{summary['maximum_c']:.1f} °C)")


def main()->None:
    """Load the bundled observations and print their summary."""
    observations=read_observations()
    summary=summarize(observations)
    print(f"Laboratory temperature report")
    print( render_report(summary) )


if __name__ == "__main__": main()
