import pandas as pd

d={
   'Age':  [31,32,33,30,29],
   'Job Tytle':['St','Ch','Dr','Ct','Se'],
   'City':['Raj','Bog','Din','Rba','Nat'],
    'Name': ['Saroar', 'Sohel', 'Ferdous', 'Delwar', 'Riyad']}

df=pd.DataFrame(d)
print(df['Name'])