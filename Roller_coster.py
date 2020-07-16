import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
wood=pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel=pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
print(wood.head())
print(steel.head())
# load rankings data here:
print(wood.info())
print(steel.info())



# write function to plot rankings over time for 1 roller coaster here:
def rank_1(coster_name,coster_park,dataframe):
  coster_rankings=dataframe[(dataframe['Name']==coster_name) & (dataframe['Park']==coster_park)]
  fig,ax=plt.subplots()
  ax.plot(coster_rankings['Year of Rank'],coster_rankings['Rank'])
  ax.set_xticks(coster_rankings['Year of Rank'].values)
  ax.set_yticks(coster_rankings['Rank'].values)
  ax.invert_yaxis()
  plt.xlabel('Year of Rank')
  plt.ylabel('Rank')
  plt.title('{} Rankings'.format(coster_name))
  plt.show()


rank_1('El Toro', 'Six Flags Great Adventure', wood)
plt.clf()

# write function to plot rankings over time for 2 roller coasters here:
def rank_2(coster_name_1,coster_park_1,coster_name_2,coster_park_2,dataframe):
  coster_ranking_1=dataframe[(dataframe['Name']==coster_name_1) & (dataframe['Park']==coster_park_1)]
  coster_ranking_2=dataframe[(dataframe['Name']==coster_name_2) & (dataframe['Park']==coster_park_2)]
  fig,ax=plt.subplots()
  ax.plot(coster_ranking_1['Year of Rank'],coster_ranking_1['Rank'])
  ax.plot(coster_ranking_2['Year of Rank'],coster_ranking_2['Rank'])
  ax.invert_yaxis()
  plt.title('{} vs {} Ranking'.format(coster_name_1,coster_name_2))
  plt.xlabel('Year of Rank')
  plt.ylabel('Rank')
  plt.legend()
  plt.show()
  

rank_2('El Toro','Six Flags Great Adventure','Boulder Dash','Lake Compounce',wood)
plt.clf()

# write function to plot top n rankings over time here:
def rank_n(dataframe,n):
  coster_ranking=dataframe[(dataframe['Rank']<=n)]
  fig,ax=plt.subplots(figsize=(10,10))
  
  for coster in set(coster_ranking['Name']):
    new_ranking=coster_ranking[coster_ranking['Name']==coster]
    ax.plot(new_ranking['Year of Rank'],new_ranking['Rank'],label=coster)
  ax.set_yticks([i for i in range(1,n)])
  ax.invert_yaxis()
  plt.title('{} ranking'.format(n))
  plt.xlabel('Year of Rank')
  plt.ylabel('Rank')
  plt.legend()
  plt.show()

rank_n(wood,5)
plt.clf()

# load roller coaster data here:
roller_coster=pd.read_csv('roller_coasters.csv')
print(roller_coster.head())


# write function to plot histogram of column values here:
def new_roller(dataframe,column_name):
  plt.hist(dataframe[column_name].dropna())
  plt.title('{} roller_coaster Histogram'.format(column_name))
  plt.xlabel(column_name)
  plt.ylabel('count')
  plt.show()

new_roller(roller_coster,'speed')
plt.clf()
new_roller(roller_coster,'length')
plt.clf()
new_roller(roller_coster,'num_inversions')
plt.clf()
new_roller(roller_coster,'height')
plt.clf()

# write function to plot inversions by coaster at a park here:
# function to plot histogram of height values
def plot_height_histogram(coaster_df):
  heights = coaster_df[coaster_df['height'] <= 140]['height'].dropna()
  plt.hist(heights)
  plt.title('Histogram of Roller Coaster Height')
  plt.xlabel('Height')
  plt.ylabel('Count')
  plt.show()

plot_height_histogram(roller_coster)
plt.clf()

# function to plot inversions by coaster at park
def plot_inversions_by_coaster(coaster_df, park_name):
  park_coasters = coaster_df[coaster_df['park'] == park_name]
  park_coasters = park_coasters.sort_values('num_inversions', ascending=False)
  coaster_names = park_coasters['name']
  number_inversions = park_coasters['num_inversions']
  plt.bar(range(len(number_inversions)),number_inversions)
  ax = plt.subplot()
  ax.set_xticks(range(len(coaster_names)))
  ax.set_xticklabels(coaster_names,rotation=90)
  plt.title('Number of Inversions Per Coaster at {}'.format(park_name))
  plt.xlabel('Roller Coaster')
  plt.ylabel('# of Inversions')
  plt.show()

plot_inversions_by_coaster(roller_coster, 'Six Flags Great Adventure')
plt.clf()




# write function to plot pie chart of operating status here:
def roller_inversion(dataframe):
  opened_roller=dataframe[dataframe['status']=='status.operating']
  closed_roller=dataframe[dataframe['status']=='status.closed.definitely']
  total_open=len(opened_roller)
  total_closed=len(closed_roller)
  total=[total_open,total_closed]
  plt.pie(total,autopct='%.1f%%',labels=['open','close'])
  plt.show()

roller_inversion(roller_coster)
plt.clf()

# write function to create scatter plot of any two numeric columns here:
# function to plot scatter of any two columns
def plot_scatter(coaster_df, column_x, column_y):
  plt.scatter(coaster_df[column_x],coaster_df[column_y])
  plt.title('Scatter Plot of {} vs. {}'.format(column_y,column_x))
  plt.xlabel(column_x)
  plt.ylabel(column_y)
  plt.show()

# function to plot scatter of speed vs height
def plot_scatter_height_speed(coaster_df):
  coaster_df = coaster_df[coaster_df['height'] < 140]
  plt.scatter(coaster_df['height'],coaster_df['speed'])
  plt.title('Scatter Plot of Speed vs. Height')
  plt.xlabel('Height')
  plt.ylabel('Speed')
  plt.show()

plot_scatter_height_speed(roller_coster)
plt.clf()
