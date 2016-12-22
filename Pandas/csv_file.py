import numpy as np
import pandas as pd
raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],
        'age': [42, 52, 36, 24, 73],
        'preTestScore': [4, 24, 31, ".", "."],
        'postTestScore': ["25,000", "94,000", 57, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])
#

## writing the output to a csv file
# print(df)
df.to_csv('../data/example.csv')
###########----############

## Reading the csv file##
read_df = pd.read_csv('../data/example.csv')
print(read_df)
print(read_df.shape)
print(read_df.describe())


###---###
