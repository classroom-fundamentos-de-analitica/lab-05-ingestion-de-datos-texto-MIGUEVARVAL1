import pandas as pd
import os
import zipfile
import csv

archivo = zipfile.ZipFile('data.zip','r')
archivo.extractall()

def create_test_and_train_dataset():
    path = ["train/", "test/"]
    output_file = ["train_dataset.csv", "test_dataset.csv"]
    folders = ["negative", "positive", "neutral"]
    i = 0
    for file in output_file:
        with open(file, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["phrase", "sentiment"])
        for folder in folders:
            folder_path =  path[i] + folder
            with open(file, "a", newline="") as csvfile:
                writer = csv.writer(csvfile)

                for filename in os.listdir(folder_path):
                    if filename.endswith(".txt"):
                        file_path = os.path.join(folder_path, filename)
                        with open(file_path, "r") as f:
                            content = f.read()
                            writer.writerow([content, folder])
        i += 1
    return


create_test_and_train_dataset()