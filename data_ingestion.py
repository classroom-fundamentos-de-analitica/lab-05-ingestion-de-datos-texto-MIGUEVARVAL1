import pandas as pd
import os

def generate_csv_files(path):
    df = {'phrase': [], 'sentiment': []}
    
    for name, _, files in os.walk(path):
        for file in files:
            if file.endswith('.txt'):
                with open(os.path.join(name, file), 'r') as f:
                    df['phrase'].append(f.read())
                    df['sentiment'].append(os.path.basename(name))

    df = pd.DataFrame(df) 
    df.to_csv(f'{os.path.basename(path)}_dataset.csv', index=False)

folders = ['data/train', 'data/test']

for folder in folders:
    generate_csv_files(folder)
