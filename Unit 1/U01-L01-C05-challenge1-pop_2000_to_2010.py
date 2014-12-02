# The data world is now your oyster. Play with some of the other population
# data and see what you come up with. Try and calculate the population change
# between 2010 and 2100. Remember the lesson about doing integer divison.
# Convert one of the numbers to floating point decimal by using the float()
# function. Which continent is estimated to grow the most in the next 90
# years?


from collections import defaultdict

population_dict = defaultdict(int)

with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:

	header = next(inputFile)

	for line in inputFile:
	  line = line.rstrip().split(',')
	  pop2000 = int(line[4])
	  pop2010 = int(line[5])
	  if line[1] == 'Total National Population':
	  	population_change = pop2010 - pop2000
	  	population_dict[line[0]] += population_change #line[0] is the continent
	inputFile.close()

with open('U01-L01-C05-challenge1-pop_2000_to_2010.csv', 'w') as outputFile:
	outputFile.write('continent, population_difference_between_2010_and_2000\n')

	for k,v in population_dict.iteritems():
		outputFile.write(k + ',' + str(v) + '\n')

