import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#% matplotlib inline


# read in the data using pandas
city_df = pd.read_csv('C:/Users/Sal/Desktop/homework-instructions/05-Matplotlib/Instructions/Pyber/data/city_data.csv')
ride_df = pd.read_csv('C:/Users/Sal/Desktop/homework-instructions/05-Matplotlib/Instructions/Pyber/data/ride_data.csv')

# inspect the dataset
city_df.head()

ride_df.head()

# combine the two tables
merged_df = pd.merge(ride_df, city_df, how="left", on="city")

merged_df.head(10)

# filter dataframe for city type
rural_df = merged_df[merged_df["type"] == "Rural"]
suburban_df = merged_df[merged_df["type"] == "Suburban"]
urban_df = merged_df[merged_df["type"] == "Urban"]

# avg fare, ride count, driver count
rural_avg_fare = rural_df.groupby("city").mean()["fare"]
rural_driver_count = rural_df.groupby("city").mean()["driver_count"]
rural_ride_count = rural_df.groupby("city").count()["ride_id"]

# avg fare, ride count, driver count
suburban_avg_fare = suburban_df.groupby("city").mean()["fare"]
suburban_driver_count = suburban_df.groupby("city").mean()["driver_count"]
suburban_ride_count = suburban_df.groupby("city").count()["ride_id"]

# avg fare, ride count, driver count
urban_avg_fare = urban_df.groupby("city").mean()["fare"]
urban_driver_count = urban_df.groupby("city").mean()["driver_count"]
urban_ride_count = urban_df.groupby("city").count()["ride_id"]


# plot the rural
plt.scatter(x=rural_ride_count, y=rural_avg_fare, s=10*rural_driver_count, 
            c='gold', marker='o', alpha=0.8, 
            linewidths=1, edgecolors="black", label="rural")

# plot the surburban
plt.scatter(x=suburban_ride_count, y=suburban_avg_fare, s=10*suburban_driver_count, 
            c='skyblue', marker='o', alpha=0.8, 
            linewidths=1, edgecolors="black", label="suburban")

# plot the urban
plt.scatter(x=urban_ride_count, y=urban_avg_fare, s=10*urban_driver_count, 
            c='coral', marker='o', alpha=0.8, 
            linewidths=1, edgecolors="black", label="urban")

plt.title("Avg Fare vs Numbers of Rides")
plt.xlabel('Number of Rides per City')
plt.ylabel('Average Fare Per City ($)')
plt.legend(loc='best')

plt.savefig("C:/Users/Sal/Desktop/pyber_work/scatter_city_type.png")

#Fares average by city
fares_by_city_type = merged_df.groupby('type').sum()['fare']

# Labels for the sections of our pie chart
labels = ["Rural", "Suburban", "Urban"]

# The values of each section of the pie chart
sizes = [4327.93, 19356.33, 39854.38]

# The colors of each section of the pie chart
colors = ["gold", "skyblue", "lightcoral"]

# Tells matplotlib to seperate the "Python" section from the others
explode = (0, 0, 0.2)
# Creates the pie chart based upon the values above
# Automatically finds the percentages of each part of the pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct="%1.1f%%", shadow=True, startangle=140)

plt.title("% of Total Fares by City Type")

plt.savefig("C:/Users/Sal/Desktop/pyber_work/fares_by_type.png")

#Riders per city
riders_per_city_type= merged_df.groupby('type').count()['ride_id']

# Labels for the sections of our pie chart
labels = ["Rural", "Suburban", "Urban"]

# The values of each section of the pie chart
sizes = [125, 625, 1625]

# The colors of each section of the pie chart
colors = ["gold", "skyblue", "lightcoral"]

# Tells matplotlib to seperate the "Python" section from the others
explode = (0, 0, 0.2)

# Creates the pie chart based upon the values above
# Automatically finds the percentages of each part of the pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct="%1.1f%%", shadow=True, startangle=140)
plt.title("% of Total Rides by City Type")

plt.savefig("C:/Users/Sal/Desktop/pyber_work/rides_by_city_type.png")

#Driver per city
drivers_per_city_type= city_df.groupby('type').sum()['driver_count']

# Labels for the sections of our pie chart
labels = ["Rural", "Suburban", "Urban"]

# The values of each section of the pie chart
sizes = [78, 490, 2405]

# The colors of each section of the pie chart
colors = ["gold", "skyblue", "lightcoral"]

# Tells matplotlib to seperate the "Python" section from the others
explode = (0, 0, 0.2)

# Creates the pie chart based upon the values above
# Automatically finds the percentages of each part of the pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct="%1.1f%%", shadow=True, startangle=140)
plt.title("% of Total Drivers by City Type")

plt.savefig("C:/Users/Sal/Desktop/pyber_work/drivers_by_city_type.png")

print("Finished")