import sys
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("filepath", help="input file path", type=str)
parser.add_argument("wordlist_path", help="path to a list of words", type=str)
args = parser.parse_args()

mywordlist = open(args.wordlist_path,'r').read()

def check_word(input, wordlist):
	for item in re.findall('[a-zA-Z]{5,}',input):
		if ( item.lower() in wordlist ):
			print "matched string:",item
			return 1
	return 0

key = '''+6.*+6%.+.6*%"#$$,!+.6&$6*+&$3'''
keys = list()
for i in range(len(key)):
	keys.append(key[i:len(key)]+key[0:i])
	
f = open(args.filepath,'r')

for line in f:
	print "----LINE----",line.strip()
	input = line.strip()
	if ( (input != "") and (input != "####") ):
		for rkey in keys:
			output = ""
			for j in range(len(input)):
				output = output +chr(ord(input[j])^ord(rkey[j%len(rkey)]))
			if ( check_word(output,mywordlist) == 1):
				print "KEY:"+rkey
				print output
				print "********************"

f.close
