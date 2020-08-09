import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt

healthcare = pd.read_csv("healthcare.csv")
print(healthcare.head())
print(healthcare["DRG Definition"].unique())
print(healthcare.shape)
chest_pain = healthcare[healthcare['DRG Definition'] == '313 - CHEST PAIN']
alabama_chest_pain = chest_pain[chest_pain['Provider State'] == "AL"]
costs = alabama_chest_pain[' Average Covered Charges '].values
print(chest_pain)
plt.boxplot([costs],labels=['costs'])
plt.show()
plt.clf()
states=healthcare['Provider State'].unique()
print(states)
datasets = []
for state in states:
  datasets.append(chest_pain[chest_pain['Provider State'] == state][' Average Covered Charges '].values)
plt.figure(figsize=(20,6))
plt.boxplot(datasets)
plt.show()
