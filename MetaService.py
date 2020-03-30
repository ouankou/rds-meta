import json
import re
import sys
import random

def majorityVote(obj):
	VoteNum = 0
	jsAry = []
	finalAry = []
	for i in range(len(obj)):
		if obj[i] != None :
			js = {}
			VoteNum += 1
			for key in obj[i].keys():
				if obj[i][key] == {}:
					js[i] = "no race"
				for key1 in obj[i][key].keys():
					if obj[i][key][key1] != {}:
						js[i] = obj[i][key][key1]
						break;
					else:
						js[i] = 'no race'
			jsAry.append(js)
	vote = 0
	for item in jsAry:
		for key in item.keys():
			 vote += 1
	if vote/VoteNum >= 0.5:
		print("RDS detected a data race by majority vote!")
		for item in jsAry:
			for key in item.keys():
				if item[key] != 'no race':
					js = {}
					js['race'] = "true"
					js['method'] = "Majority Vote"
					js['race information'] = item[key]
					finalAry.append(js)
	else:
		print("No data race find")
	js = {}
	for i in range(len(finalAry)):
		js[i] = finalAry[i]

	#r = json.dumps(js)
	r = js
	return(r)

def weightVote(obj):

	finalAry = []

	Tsanweight = 0.25

	Archerweight= 0.25

	Inspectorweight = 0.25

	Rompweight = 0.25

	jsAry = []
	for i in range(len(obj)):
		if obj[i] != None :
			js = {}
			for key in obj[i].keys():
				if obj[i][key] == {}:
					js[i] = "no race"
				for key1 in obj[i][key].keys():
					if obj[i][key][key1] != {}:
						js[i] = obj[i][key][key1]
						break;
					else:
						js[i] = 'no race'
			jsAry.append(js)
	WeightFlag = 0

	for item in jsAry:
		for key in item.keys():
			if key == 0:
				if item[key] != 'no race':
					ArcherVote = 1
				else:
					ArcherVote = 0
			if key == 1:
				if item[key] != 'no race':
					InsepctorVote = 1
				else:
					InsepctorVote = 0
			if key == 2:
				if item[key] != 'no race':
					TsanVote = 1
				else:
					TsanVote = 0
			if key == 3:
				if item[key] != 'no race':
					RompVote = 1
				else:
					RompVote = 0

	InsepctorVote = 0

	WeightFlag = Tsanweight * TsanVote + Archerweight * ArcherVote + Inspectorweight * InsepctorVote + Rompweight * RompVote

	if WeightFlag >= 0.5:
		print("RDS detected a data race by weight vote!")
		for item in jsAry:
			for key in item.keys():
				if item[key] != 'no race':
					js = {}
					js['race'] = "true"
					js['method'] = "Weight Vote"
					js['race information'] = item[key]
					finalAry.append(js)
	else:
		print("No data race find")
	js = {}
	for i in range(len(finalAry)):
		js[i] = finalAry[i]

	#r = json.dumps(js)
	r = js
	return(r)

def randomVote(obj):
	finalAry = []
	VoteNum = 0
	jsAry = []
	for i in range(len(obj)):
		if obj[i] != None :
			js = {}
			VoteNum += 1
			for key in obj[i].keys():
				if obj[i][key] == {}:
					js[i] = "no race"
				for key1 in obj[i][key].keys():
					if obj[i][key][key1] != {}:
						js[i] = obj[i][key][key1]
						break;
					else:
						js[i] = 'no race'
			jsAry.append(js)
	
	RandomFlag = random.randint(0, VoteNum-1)
	
	for key in jsAry[RandomFlag].keys():
		if jsAry[RandomFlag][key] != 'no race':
			print("RDS detected a data race by random vote!")
			js = {}
			js['race'] = "true"
			js['method'] = "Random Vote"
			js['race information'] = jsAry[RandomFlag][key]
			finalAry.append(js)
		else:
			print("No data race find")
		js = {}
	for i in range(len(finalAry)):
		js[i] = finalAry[i]

	#r = json.dumps(js)
	r = js
	return(r)

