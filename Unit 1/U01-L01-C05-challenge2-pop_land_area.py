# Try and calculate the population density (total national population divided by
# the total land area and remember to convert at least one number to float).
# Which continent was most densely populated in 2010?

from collections import defaultdict
import csv

population_dict = defaultdict(dict)

with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
	inputReader = csv.reader(inputFile)
	header = next(inputFile)
	for line in inputReader:
		continent = str(line[0])
		urbanrural = str(line[2])
		pop2010 = int(line[5])
		landarea = float(line[7])
		if line[1] == 'Total National Population':
			population_dict[continent][urbanrural] = pop2010/landarea
	
with open('U01-L01-C05-challenge2-pop_land_area.csv', 'w') as outputFile:
	outputFile.write('continent, urbanrural, density\n')
	for k, v in population_dict.iteritems():
		for c in v.iteritems():
			outputFile.write(str(k) + ',' + str(c[0]) + ',' + str(c[1]) + '\n')