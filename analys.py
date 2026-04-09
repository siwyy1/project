import pandas as pd

#Data Frame
df = pd.read_csv("students.csv")


#mask
grade_mask = df['Grade'] > 90
subject_mask = df['Subject'] == "Math"

print(df[subject_mask & grade_mask])
