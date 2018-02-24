# import csv
# import json

# def main():

# 	Trucks= {}
# 	for i in range(6):
# 		with open('Snowplow' + str(i) +'.csv')as csvfile:
# 			reader = csv.reader(csvfile, delimiter=',')
# 			for row in reader:
# 				reader1 = csv.reader(csvfile, delimiter=',')
# 				Trucks[row[1]] = {}
# 				for row1 in reader1:
# 					Trucks[row[1]][row1[3]] = (row1[7],row1[8],row1[4])
# 				##Trucks[row[1]] = {row[3]:(row[7], row[8], row[4])}




# 	print(json.dumps(Trucks, indent=1))


# if __name__ == "__main__":
# 	main()

import csv
import json
import pandas as pd


##Trucks= {}
##df = pd.read_csv('Snowplow0'+str(i)+'.csv')
##for 
##Trucks[df.iloc[row, column]].append(time[df.iloc[row,column]])

def Database():
	Trucks = {}
	for i in range(6):
		with open('Snowplow' + str(i) +'.csv')as csvfile:
			reader = csv.reader(csvfile, delimiter=',')
			firstline = True
			for row in reader:
				if firstline:
					firstline = False
					continue
				truck_id = row[1].replace(" ", "")
				truck_id = row[1].replace(".", "")
				truck_id = int(truck_id)
				time = row[3]
				longa = float(row[7])
				lang = float(row[8])
				orien = row[4]
				orien = row[4]
				Trucks[time] = (truck_id, longa, lang, orien)
	return(Trucks)


print(Database())