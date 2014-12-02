# Try and calculate the population density (total national population divided by
# the total land area and remember to convert at least one number to float).
# Which continent was most densely populated in 2010?

from collections import defaultdict
import csv

population_dict = {} # simple plain dictionary

with open('lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
  inputReader = csv.reader(inputFile) # good use of the csv_reader! Makes life a lot easier. 
  header = next(inputFile) 
  
  for line in inputReader:
    continent = line[0] # no need to convert to a string, as it is already in that format.
    urbanrural = line[2] # same with the rural / urban
    pop2010 = int(line[5])
    landarea = float(line[7])
  
    if line[1] == 'Total National Population':
      # tests to see if the continent is not already a key value the population_dict
      if line[0] not in population_dict: 
        # create the continent key and link it to the defaultdict  
        population_dict[line[0]] = defaultdict(int) 
      # now that we know the key exists with the defaultdict, add the pop & area
      population_dict[continent]['pop'] += pop2010 
      population_dict[continent]['area'] += landarea

# print out the results
for k, v in population_dict.iteritems():
  print "Continent: {}\nPop: {}\nArea: {}\nDensity:{}\n".format(k, v['pop'], v['area'], round(v['pop']/v['area'],2))

# if any of the above code doesn't make sense, you find a bug in my code/logic, or you think of a different way to approach it email me! 

# I'll leave it to you to re-write the file output part with the nested new dictionary. :)
# with open('U01-L01-C05-challenge2-pop_land_area.csv', 'w') as outputFile:
#   outputFile.write('continent, urbanrural, density\n')
#   for k, v in population_dict.iteritems():
#     for c in v.iteritems():
#       outputFile.write(str(k) + ',' + str(c[0]) + ',' + str(c[1]) + '\n')
