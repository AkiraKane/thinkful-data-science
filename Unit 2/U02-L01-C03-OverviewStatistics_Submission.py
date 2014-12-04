import pandas as pd
from scipy import stats

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

# First, split the string on the (hidden characters that indicate) newlines
data = data.splitlines() # we could also do data.split('\n')

# Then, split each item in this list on the commas
# the bracketed expression is a list comprehension
data = [i.split(', ') for i in data] 

# Now, convert create a pandas dataframe
column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

# Convert Alcohol and Tobacco columns to float
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

print "The mean of alcohol is " + str(df['Alcohol'].mean())
print "The median of alcohol is " + str(df['Alcohol'].median())
print "The mode of alcohol is " + str(stats.mode(df['Alcohol']))
print "\n"
print "The mean of tobacco is " + str(df['Tobacco'].mean())
print "The median of tobacco is " + str(df['Tobacco'].median())
print "The mode of tobacco is " + str(stats.mode(df['Tobacco']))
print "\n"
# range: the difference between the largest and smallest values of a set 
print "The range of alcohol is " + str(max(df['Alcohol']) - min(df['Alcohol']))
# standard deviation: the square root of the variance, sigma or s.
print "The standard deviation of alcohol is " + str(df['Alcohol'].std())
# variance: the measure of how data points are distributed about the distributions mean
# (i.e., how the data points are distirubted about the center). The variance sigma^2 of 
# a population is found by taking the sum of (x - mu)^2 for all values of x, and dividing 
# by the number of data points. The variance of a sample s^2 is found by taking the sum 
# of (x - xbar)^2 for all values of x, and dividing by the number of data points - 1.
print "The variance of alcohol is " + str(df['Tobacco'].var())
print "\n"
# range: the difference between the largest and smallest values of a set 
print "The range of tobacco is " + str(max(df['Tobacco']) - min(df['Tobacco']))
# standard deviation: the square root of the variance, sigma or s.
print "The standard deviation of tobacco is " + str(df['Tobacco'].std())
# variance: the measure of how data points are distributed about the distributions mean
# (i.e., how the data points are distirubted about the center). The variance sigma^2 of 
# a population is found by taking the sum of (x - mu)^2 for all values of x, and dividing 
# by the number of data points. The variance of a sample s^2 is found by taking the sum 
# of (x - xbar)^2 for all values of x, and dividing by the number of data points - 1.
print "The variance of tobacco is " + str(df['Tobacco'].var())