import numpy as np
import pandas as pd
# type your code here
words_list = ['words', 'will', 'where', 'shall', 'we', 'will', 'shall', 'we', 'words', 'where', 'shall',
            'will', 'there', 'wow', 'should', 'shall', 'we', 'where', 'should', 'where', 'will', 
            'there', 'now', 'where', 'we', 'will', 'where', 'should', 'will', 'where']

words_data_frame = pd.DataFrame(words_list)
words_data_frame

counts_words = words_data_frame.value_counts()
counts_words.iloc[0:5]
