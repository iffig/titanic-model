import pandas as pd
import os 

path = os.path.join("titanic", "train.csv")
print(path)

df = pd.read_csv(path)

print(df.to_string()) 