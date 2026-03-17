# Wooclap Data Internship Tech Case - 2026

**Layal Baydoun**

## Setup

```bash
# Create and activate virtual environment
python -m venv wooclap_assessment_venv
wooclap_assessment_venv\Scripts\activate

# Install dependencies
pip install pandas numpy pyarrow path
```

## Project Structure

```
data/           # Raw input files (sample.csv, metadata.csv)
src/
  main.py       # Entry point — runs all exercises
  exercises/
    exercise_1.py
    exercise_2.py
out/            # Generated output (created at runtime)
```

## How to Run

```bash
cd src
python main.py
```

## Exercises

### Exercise 1 — Data Formatting

Reads `data/sample.csv`, parses the `created_at` timestamp, extracts the date, and writes the dataset to Parquet format partitioned by day into `out/sample.parquet/`.

### Exercise 2 — Data Exploration (Part 1)

Reads the Parquet file produced by Exercise 1 and generates `out/exercise_2_distribution.png`, a 4-panel figure analysing the distribution of answers over time:

- **Answers per Day** — bar chart showing daily answer volume across the full dataset period (Aug 2018 – Jan 2019). Activity peaks in October 2018.
- **Answers by Hour of Day (UTC)** — bar chart revealing that most answers are submitted between 07:00 and 15:00 UTC, consistent with daytime classroom usage.
- **Answers per Month** — scatter plot confirming that October and November concentrate the highest answer volumes, likely corresponding to the academic semester peak.
- **Answers by Day of Week (Kiviat/radar chart)** — shows answers are heavily concentrated on weekdays (Mon–Thu), with a sharp drop on weekends, as expected for classroom activity.

## AI Disclosure
