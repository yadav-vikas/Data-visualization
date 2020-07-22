import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

#WORLD CUP DATA
df=pd.read_csv('WorldCupMatches.csv')
#print(df.head())
df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']
print(df)
print(df.columns)
sns.set_style('whitegrid')
sns.set_context('poster')
f, ax = plt.subplots(figsize=(12,10))
ax=sns.barplot(x='Year',y='Total Goals', data=df)
ax.set_title('World Cup Data analysis')

plt.show()
#GOALS DATA 
goals=pd.read_csv('goals.csv')
print(df.head())
sns.set_context('notebook',font_scale=1.25)
f,ax2=plt.subplots(figsize=(12,7))
# Save a palette to a variable:
palette = sns.color_palette("spectral")
# Use palplot and pass in the variable:
sns.palplot(palette)
ax2=sns.boxplot(data=goals,x='year',y='goals')
plt.title('Goals vs year anaylysis')
plt.show()
