import numpy as np
import pandas as pd

institute= ['Institute_A' , 'Institute_B' ]
subjects = ['Machine Learning' , 'Python' ]
mindex = pd.MultiIndex.from_product([institute,subjects])
data=([[12,45,67,56],[78,89,45,67],[45,67,89,90],[67,44,56,55]])
df_student = pd.DataFrame(data=data, index=['Studen_1', 'Student_2', 'Student_3', 'Student_4'], columns=mindex)
df_student
df_student.stack(level=0)
