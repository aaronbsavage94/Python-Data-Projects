#import necessary modules
import pandas as ps
# import the seaborn module
import seaborn as sns
# import the matplotlib module
import matplotlib.pyplot as plt

#csv import
csv = "VA Median House Prices.csv"
house_data = ps.read_csv(csv)

##print(house_data.head)

# set the background colour of the plot to white
sns.set(style="whitegrid", color_codes=True)
# setting the plot size for all plots
sns.set(rc={'figure.figsize':(11.7,8.27)})
# create a countplot
sns.barplot(x='Year',y='Median Price',data=house_data, hue='State')
# Remove the top and down margin
sns.despine(offset=10, trim=True)
# display the plotplt.show()

plt.show()