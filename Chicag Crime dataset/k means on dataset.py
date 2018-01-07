"""
Explore the City of Chicago's Crime data set, which is part of their Open Data initiative.
"""
import pandas as pd

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
import geoplotlib


# Look Pretty
plt.style.use('ggplot')


#
# To procure the dataset, follow these steps:
# 1. Navigate to: https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2
# 2. In the 'Primary Type' column, click on the 'Menu' button next to the info button,
#    and select 'Filter This Column'. It might take a second for the filter option to
#    show up, since it has to load the entire list first.
# 3. Scroll down to 'GAMBLING'
# 4. Click the light blue 'Export' button next to the 'Filter' button, and select 'Download As CSV'


def doKMeans(df):
  #
  # INFO: Plot data with a '.' marker, with 0.3 alpha at the Longitude,
  # and Latitude locations in your dataset. Longitude = x, Latitude = y
  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.scatter(df.lon, df.lat, marker='.', alpha=0.1)

  #
  # : Filter df so that you're only looking at Longitude and Latitude,
  # since the remaining columns aren't really applicable for this purpose.
  #
  sliceK = df[['lon', 'lat']]


  #
  # : Use K-Means to try and find seven cluster centers in this df.
  #

  #model = KMeans(n_clusters=10, n_init=10, init='k-means++')
  model = DBSCAN(eps=0.5, min_samples=5, metric="euclidean",metric_params=None, algorithm="auto",leaf_size=30, p=None, n_jobs=1)
  model.fit(sliceK)

  #
  # INFO: Print and plot the centroids...
  centroids = model.cluster_centers_
  try:
    geoplotlib.dot(df, color='red', point_size=0.2)
  except:
      print("Exception")
  geoplotlib.show()
  
  ax.scatter(centroids[:,0], centroids[:,1], marker='x', c='red', alpha=0.5,
             linewidths=3, s=169)

  print (centroids)



#
# : Load  dataset after importing Pandas
#
df = pd.read_csv('''InputFileNameHere''', index_col="IUCR")

#
# : Drop any ROWs with nans in them
#
df.dropna(inplace=True)

#
# : Print out the dtypes of your dset
#
print ('describe --->',df.describe())
print('types---->',df.dtypes)

#
# Coerce the 'Date' feature (which is currently a string object) into real date,
# and confirm by re-printing the dtypes. NOTE: This is a slow process...
#
#df.Date = pd.to_datetime(df.Date, errors='coerce')
#print('---> after cooerce',df.dtypes)


# INFO: Print & Plot your data
doKMeans(df)


#
# : Filter out the data so that it only contains samples that have
# a Date > '2011-01-01', using indexing. Then, in a new figure, plot the
# crime incidents, as well as a new K-Means run's centroids.
#
#df2 = df[df.Date > '2017-01-01']


# INFO: Print & Plot your data
#doKMeans(df2)
plt.show()