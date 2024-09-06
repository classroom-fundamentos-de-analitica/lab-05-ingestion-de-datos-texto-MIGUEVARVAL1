import pandas as pd
import os.path


def test_train_dataset_exists():
    assert os.path.exists("train_dataset.csv"), "File 'train_dataset.csv' not found"


def test_train_dataset_columns():
    train_dataset = pd.read_csv("train_dataset.csv")
    assert train_dataset.columns[0] == "phrase"
    assert train_dataset.columns[1] == "sentiment"


def test_train_dataset_value_counts():
    train_dataset = pd.read_csv("train_dataset.csv")
    counts = train_dataset["sentiment"].value_counts()
    assert counts["neutral"] == 1117
    assert counts["positive"] == 458
    assert counts["negative"] == 236


def test_test_dataset_exists():
    assert os.path.exists("test_dataset.csv"), "File 'test_dataset.csv' not found"


def test_test_dataset_value_counts():
    test_dataset = pd.read_csv("test_dataset.csv")
    counts = test_dataset["sentiment"].value_counts()
    assert counts["neutral"] == 274
    assert counts["positive"] == 112
    assert counts["negative"] == 67
