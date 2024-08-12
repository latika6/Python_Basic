# type your code here
import numpy as np
import pandas as pd
name = ['Emma Larter', 'Mia Junior', 'Sophia Depp', 'James Smith']
salary = [3200, 4500, 3600, 5596]
df = pd.DataFrame({'Name': name, 'Salary': salary})
df

df[['First_name', 'Last_name']] = df.Name.str.split(expand=True)
df
