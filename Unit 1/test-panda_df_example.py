import csv
import pandas as pd

df = pd.read_csv('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv')

query = df[(df["Continent"] == "Asia") & (df["ElevationZone"] == "Total National Population")]

row_iterator = query.iterrows()

msg = ""
for index, row in row_iterator:	
	print index
	print row['Continent']	
	msg = msg + row['Continent'] + ' ,' + row['UrbanRuralDesignation'] + ', '
	print msg
