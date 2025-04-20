# Script to download the GRID Corpus Dataset from Kaggle: 
import os
os.system("pip install kagglehub")


import kagglehub

# Download latest version
path = kagglehub.dataset_download("jedidiahangekouakou/grid-corpus-dataset-for-training-lipnet")

print("Path to dataset files:", path)

os.system(f"mv {path} ./GRIDCorpus")