import pandas as pd
import matplotlib.pyplot as plt

web_stats={
    'Day':[1,2,3,4,5,6,7,8],
    'Visitors':[54,66,88,45,75,78,88,99],
    'Bouncer':[58,66,88,11,22,44,55,66]

}

df=pd.DataFrame(web_stats)
print(df)
print(df.head())  ## prints th first 5
print(df.tail())    ## prints the last 5
print(df.tail(2))
print('The Days are as follows')
print(df['Day'])

