import os 
import shutil

from exercises.exercise_1 import run_exercise_1
from exercises.exercise_2_part_1 import run_exercise_2
from exercises.exercise_2_part_2 import run_exercise_2_part_2

def prepare_out_folder(out_folder_path):
    # make sure out folder is empty before writing the parquet file
    if os.path.exists(out_folder_path):
        shutil.rmtree(out_folder_path)
        os.makedirs(out_folder_path)
    else:
        os.makedirs(out_folder_path)

if __name__ == "__main__":
    # Run script of exercise 1
    data_folder_path = "data"    
    out_folder_path = "out"

    # make sure out folder is empty before writing the parquet file
    print("Making sure the output folder is empty before writing the parquet file...")
    prepare_out_folder(out_folder_path)

    # Run the exercise 1 script
    print("Running Exercise 1 script...")
    run_exercise_1(data_folder_path, out_folder_path)

    # Run the exercise 2 script
    print("Running Exercise 2 script...")
    run_exercise_2(out_folder_path + "/")
