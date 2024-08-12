# type your code here
import pandas as pd
df_store = pd.DataFrame(
{
'Store': ['A', 'B', 'A', 'C', 'D', 'A', 'D', 'A', 'C', 'B'],
'Location': ['Mumbai', 'Pune', 'Hyderabad', 'Mumbai', 'Pune', 'Delhi', 'Hyderabad', 'Pune', 'Mumbai', 'Pune'],
'Sales': [40000, 45000, 56000, 90000, 89000, 87000, 85000, 78000, 89000, 70000]
}
)
df_store
df_store.sort_values(by = 'Sales', ascending=False)