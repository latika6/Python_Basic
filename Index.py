import pandas as pd
import numpy as np
flavours= ['vanilla' , 'chocolate' ]

cup_size = ['small' , 'medium' ]
mindex = pd.MultiIndex.from_product([flavours,cup_size])
mindex
no_of_icecreams_sold=([[12,45,67,56],
[78,89,45,67],
[45,67,89,90],
[67,44,56,55]])
df_icecream_sold = pd.DataFrame(data=no_of_icecreams_sold,
index=['Stall_1','Stall_2','Stall_3','Stall_4'] , columns=mindex
)
df_icecream_sold
