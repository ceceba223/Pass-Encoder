import json

def format_txt(text):						#format password
	text = text.replace(" ", "")			#remove 'spaces'
	text = text.lower()						#convet all letters to lower case
	return(text)							#return formated text

def encode(clear):							#encode password by rule
	with open('rule.json') as rule_json:	#open the rule .json file
		rule = json.load(rule_json)			#load file content
	i = 0									#set up increment counter 
	for c in rule[0]['to_replace']:													#for [letter defined in to_replace]
		clear = clear.replace(rule[0]['to_replace'][i], rule[1]['replacement'][i])	#replace the charater [to_replace] with the character in [replacement]
		i += 1																		#increment
	rule_json.close()						#close rule.json
	encoded = clear							#rename var
	return(encoded) 						#return encoded password

