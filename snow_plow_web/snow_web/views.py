# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import csv
import json
import pandas as pd
# Create your views here.

def organize_data():
    Trucks = {}
	for i in range(11):
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