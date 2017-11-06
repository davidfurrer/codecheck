import csv
import pandas
import distance

def spellcheck(word, n = 1000):

	wordlist = getList(n)

	return (word, wordlist)

def getList(n):
	freqFile = "word_freq.csv"
	wordlist = []
	with open(freqFile, 'rU') as readfile:
		reader = csv.reader(readfile)
		for row in reader:
			for word in row[0:n]:
				if "+" in word:
					wordlist.extend([s.lower().replace(" ", "") for s in word.split("+")])
				else:
					word.append(word.lower().replace(" ", ""))

	return wordlist

def hasMatch(word, wordlist):
	word = word.lower().replace(" ", "")
	minDis = float("inf")

	for item in wordlist:
		dis = distance.levenshtein(word, item)
		minDis = min(dis, maxDis)

	return minDis == 0