import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np

# Reading in the dataset
df = pd.read_csv('res_average_employee_benefit_cost_comparison_rc3m-jvyy.csv')

# setting the width of each bar and setting the y series
barWidth = 0.25
r1 = np.arange(len(df['Benefit']))
r2 = [x + barWidth for x in r1]


print(df.dtypes)
plt.figure(figsize=(8,5))

df['Market Contribution'] = df['Market Contribution'].astype(str)
for index, row in df.iterrows():
	df.loc[index, 'Market Contribution'] = row['Market Contribution'][1:]
	df.loc[index, 'State of Oklahoma Contribution'] = row['State of Oklahoma Contribution'][1:]

df['Market Contribution'] = df['Market Contribution'].astype(float)
df['State of Oklahoma Contribution'] = df['State of Oklahoma Contribution'].astype(float)
print(df.dtypes)

plt.barh(y=r1, 
	width=df['Market Contribution'], 
	height=barWidth, 
	edgecolor='white', 
	label='Market')
plt.barh(y=r2, 
	width=df['State of Oklahoma Contribution'], 
	height=barWidth, 
	edgecolor='white', 
	label='State of OK')

plt.ylabel('Contributor')
plt.xlabel('Dollars Contributed')
plt.yticks([r + barWidth for r in range(len(df['Benefit']))], df['Benefit'].unique().tolist(), rotation=50)
plt.legend()
plt.show()