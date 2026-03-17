# ==========================
# Exercise 1
# ==========================

# Create a script to write the CSV dataset in parquet format 
# using a partitioning per day 

import pandas as pd
from pathlib import Path

def run_exercise_1(data_folder_path, out_folder_path):
    # Make sure path exists 
    data_file = Path(data_folder_path) / "sample.csv"
    
    if not data_file.exists():
        print("The dataset file does not exist. Please make sure the path is correct.")
        return

    if not Path(out_folder_path).exists():
        print("The output folder does not exist. Please make sure the path is correct.")
        return

    # Read the CSV dataset
    df = pd.read_csv(data_file)   

    # df has cols : "type","participant_id","event_id","created_at","object_id"
    # Parse the timestamps with timezone
    df["created_at"] = pd.to_datetime(df["created_at"], format="ISO8601", utc=True)
    
    # Extract derived columns for analysis
    df["date_only"] = df["created_at"].dt.date
    df["hour"] = df["created_at"].dt.hour
    df["day_of_week"] = df["created_at"].dt.day_name()
    df["month"] = df["created_at"].dt.strftime("%Y-%m") 

    # Convert to parquet format, partitioning by the "date_only" column
    df.to_parquet(Path(out_folder_path) / "sample.parquet", partition_cols=["date_only"], index=False)

    # Done 
    print("Done writing the parquet file with partitioning by day")








