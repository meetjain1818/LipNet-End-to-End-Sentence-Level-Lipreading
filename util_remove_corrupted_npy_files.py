import numpy as np
import os
import glob

def remove_corrupted_npy_files(all_files:list, remove_corrupted:bool = False):
    if not all_files:
        print("No .npy files found. Make sure BASE_PROCESSED_PATH is correct.")
    else:
        print(f"Found {len(all_files)} files. Checking shapes...")
        for npy_file in all_files:
            try:
                data = np.load(npy_file)
                if data.ndim != 4 or data.shape[:] != TARGET_SHAPE_LAST_DIMS:
                    print(f"PROBLEM: {npy_file} has shape {data.shape}")
                    problem_files.append(npy_file)
            except Exception as e:
                print(f"ERROR reading {npy_file}: {e}")
                problem_files.append(npy_file)
    
        if not problem_files:
            print("All checked .npy files seem to have correct H, W, C dimensions.")
        else:
            print(f"\nFound {len(problem_files)} files with potential shape issues.")
            # Optionally, you could delete or reprocess these problem files
            for f_path in problem_files:
                os.remove(f_path)
            print("Problematic files removed. Please re-run preprocessing.")