#------------1
import codecademylib
from matplotlib import pyplot as plt
import pandas as pd

restaurants = pd.read_csv('restaurants.csv')

print(restaurants.head())

cuisine_options_count = restaurants.cuisine.nunique()

cuisine_counts = restaurants.groupby('cuisine').name.count().reset_index()

print(cuisine_counts)


#-----------2

import codecademylib3
from matplotlib import pyplot as plt
import pandas as pd

restaurants = pd.read_csv('restaurants.csv')

cuisine_counts = restaurants.groupby('cuisine')\
                            .name.count()\
                            .reset_index()
                          
counts=cuisine_counts.name.values
cuisines=restaurants.cuisine.unique()
print(cuisines)
print(counts)
plt.pie(counts,labels=cuisines,shadow=True,autopct='%d%%')
plt.axis('equal')
plt.show()


#-----------3

import codecademylib
from matplotlib import pyplot as plt
import pandas as pd

orders = pd.read_csv('orders.csv')

print orders.head()

orders['month'] = orders.date.apply(lambda x: x.split('-')[0])

print orders.head()

avg_order = orders.groupby('month').price.mean().reset_index()

std_order = orders.groupby('month').price.std().reset_index()

#---------4

import codecademylib
from matplotlib import pyplot as plt
import pandas as pd

orders = pd.read_csv('orders.csv')

orders['month'] = orders.date.apply(lambda x: x.split('-')[0])

avg_order = orders.groupby('month').price.mean().reset_index()

std_order = orders.groupby('month').price.std().reset_index()

ax = plt.subplot()

bar_heights = avg_order.price
bar_errors = std_order.price

plt.bar(range(len(bar_heights)),
  			bar_heights,
        yerr=bar_errors,
       capsize=5)
ax.set_xticks(range(len(bar_heights)))
ax.set_xticklabels(['April', 'May', 'June', 'July', 'August', 'September'])
plt.ylabel('Average Order Amount')
plt.title('Order Amount over Time')
plt.show()


#----------5

import codecademylib
from matplotlib import pyplot as plt
import pandas as pd

orders = pd.read_csv('orders.csv')

customer_amount = orders.groupby('customer_id').price.sum().reset_index()

print customer_amount.head()

plt.hist(customer_amount.price.values,
        range=(0, 200), bins=40)
plt.xlabel('Total Spent')
plt.ylabel("Number of Customers")
plt.title('Customer Expenditure Over 6 Months')

plt.show()
