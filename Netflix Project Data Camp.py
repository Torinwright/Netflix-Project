#!/usr/bin/env python
# coding: utf-8

# In[127]:
#project about seeing if movie lengths have changed overtime in the last 10 years

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#step 1
'''years = [2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

movies_dict = {'years': years, 'durations': durations}

#print(movies_dict)


#step 2
durations_df = pd.DataFrame(movies_dict)

#print(durations_df)

#step 3
#fig is the size of the blank graph or background
fig = plt.figure()
plt.plot(durations_df['years'], durations_df['durations'])
plt.title("Netflix Movie Durations 2011-2020")
plt.show()'''

#step 4
netflix_df = pd.read_csv("netflix_data.csv")

netflix_df[0:5]

#step 5

# Subset the DataFrame for type "Movie"
netflix_df_movies_only = netflix_df[netflix_df["type"] == "Movie"]
    
#print(netflix_df_movies_only)


# Select only the columns of interest
netflix_movies_col_subset = netflix_df_movies_only[['title', 'country', 'genre', 'release_year', 'duration']]
#print(netflix_movies_col_subset)

#print(netflix_movies_col_subset[0:5])

#step 6

'''fig = plt.figure(figsize=(12,8))
# Create a scatter plot of duration versus year
plt.scatter(netflix_movies_col_subset['release_year'],netflix_movies_col_subset['duration'])

# Create a title
plt.title("Movie Duration by Year of Release")

# Show the plot
plt.show()'''

#step 7 

# Filter for durations shorter than 60 minutes
short_movies = netflix_movies_col_subset[netflix_movies_col_subset['duration'] < 60]
    

# Print the first 20 rows of short_movies
#print(short_movies[0:20])

#step 8

# Define an empty list
colors = []

# Iterate over rows of netflix_movies_col_subset
for lab, row in netflix_movies_col_subset.iterrows() :
    
    if row['genre'] == 'Children':
        colors.append('red')
    elif row['genre'] == "Documentaries" :
        colors.append('blue')
    elif row['genre'] == "Stand-Up" :
        colors.append('green')  
    else:
        colors.append('black')
        
# Inspect the first 10 values in your list        print(netflix_movies_col_subset)
#colors[0,10]

#step 9
# Set the figure style and initalize a new figure
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus release_year
plt.scatter(netflix_movies_col_subset["release_year"], netflix_movies_col_subset["duration"], c=colors)

# Create a title and axis labels
plt.title("Movie duration by year of release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")

# Show the plot
plt.show()

#step 10
#are_movies_getting_shorter = "no"


# In[ ]:





# In[ ]:





# In[ ]:




