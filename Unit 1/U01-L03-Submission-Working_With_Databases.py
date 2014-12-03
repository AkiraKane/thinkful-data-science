# The sqlite3 module is used to work with the SQLite database.
import sqlite3 as lite
import pandas as pd

# Define our cities
cities = (('Las Vegas', 'NV'),
    			('Atlanta', 'GA'),
  				('New York City', 'NY'),
					('Boston', 'MA'),
					('Chicago', 'IL'),
					('Miami', 'FL'),
					('Dallas', 'TX'),
					('Seattle', 'WA'),
					('Portland', 'OR'),
					('San Francisco', 'CA'),
					('Los Angeles', 'CA'))

# Define the weather for cities
weather = (('Las Vegas', 2013, 'July', 'December'),
       		('Atlanta', 2013, 'July', 'January'),
       		('New York City', 2013, 'July', 'January'),
			    ('Boston', 2013, 'July', 'January'),
			    ('Chicago', 2013, 'July', 'January'),
			    ('Miami', 2013, 'August', 'January'),
			    ('Dallas', 2013, 'July', 'January'),
			    ('Seattle', 2013, 'July', 'January'),
			    ('Portland', 2013, 'July', 'December'),
			    ('San Francisco', 2013, 'September', 'December'),
			    ('Los Angeles', 2013, 'September', 'December'))

# Here we connect to the database. The `connect()` method returns a connection object.
con = lite.connect('U01-L03-DB_Submission.db')

with con:
  # From the connection, we get a cursor object. The cursor is what goes over the records that result from a query.
  cur = con.cursor()

  # Create tables and rows.  Drop tables first if they already exist.
  cur.execute('DROP TABLE IF EXISTS cities;')
  cur.execute('DROP TABLE IF EXISTS weather;')
  cur.execute('CREATE TABLE cities (name text, state text)'); #should we check to see if this is successful?
  cur.execute('CREATE TABLE weather (city text, year integer, warm_month text, cold_month text);') #should we check to see if this is successful?
  cur.executemany("INSERT INTO cities VALUES(?,?)", cities) 
  cur.executemany("INSERT INTO weather VALUES(?,?,?,?)", weather)

  cur.execute("SELECT name, state, year, warm_month, cold_month FROM cities INNER JOIN weather ON name = city") # How do we put this on multiple lines to make it more readable?

  rows = cur.fetchall()
  cols = [desc[0] for desc in cur.description]
  df = pd.DataFrame(rows, columns=cols)

query = df[(df["warm_month"] == "July")]

row_iterator = query.iterrows()

msg = ""
for index, row in row_iterator:	
	# print index
	# print row['state']	
	msg = msg + row['name'] + ', ' + row['state'] + ', '
print "The cities that are warmest in July are: " + msg

  

