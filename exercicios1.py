import pandas as pd

df = pd.DataFrame([78, 90, 56, 85, 60, 62, 96, 75, 62, 80])

print(df[0].sort_values())
#[56, 60, 62, 62, 75, 78, 80, 85, 90, 96]

print(df.mean(numeric_only=True))
#74.4

print(df.median(numeric_only=True))
#76.5

print(df.mode(numeric_only=True))
#[62] Unimodal