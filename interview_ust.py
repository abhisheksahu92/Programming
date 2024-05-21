import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/AjinkyaKamble07/python-django-sample/main/purchase_data_UK.csv',parse_dates = ['InvoiceDate'])
df = df[df.InvoiceDate.dt.between('2010-12-01 00:00:00','2010-12-01 23:59:59')]
print(df)