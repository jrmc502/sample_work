import pandas
df=pandas.read_csv("VoterFile10.csv")
df.drop(df.columns[0:11], axis=1)
from geopy.geocoders import ArcGIS
