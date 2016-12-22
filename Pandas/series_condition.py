
import pandas as pd
import numpy as np

age= np.array([31,32,33,30,29])
name=['Saroar', 'Sohel', 'Ferdous', 'Delwar', 'Riyad']
d={
   'Age': pd.Series(age,index=['a','b','c','d','e']),
   'Job Tytle': pd.Series(['St','Ch','Dr','Ct','Se'],index=['a','b','c','d','e']),
   'City':pd.Series(['Raj','Bog','Din','Rba','Nat'],index=['a','b','c','d','e']),
    'Name': pd.Series(['Saroar', 'Sohel', 'Ferdous', 'Delwar', 'Riyad'],index=['a','b','c','d','e'])}

df=pd.DataFrame(d)
print(df)

print(df['Age'].map(lambda x:x>30))