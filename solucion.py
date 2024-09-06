import os
import csv


def create_csv_from_directory(directory, output_file):
    data = []

    for sentiment in ["positive", "negative", "neutral"]:
        sentiment_path = os.path.join(directory, sentiment)
        if os.path.exists(sentiment_path):
            for filename in os.listdir(sentiment_path):
                if filename.endswith(".txt"):
                    file_path = os.path.join(sentiment_path, filename)
                    with open(file_path, "r", encoding="utf-8") as file:
                        phrase = file.read().strip()
                        data.append([phrase, sentiment])

    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["phrase", "sentiment"])
        writer.writerows(data)


create_csv_from_directory("data/train", "train_dataset.csv")

create_csv_from_directory("data/test", "test_dataset.csv")
