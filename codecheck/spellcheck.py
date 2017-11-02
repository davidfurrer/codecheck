import csv

def spellcheck(file, n):
	wordlist = getList(n)
	


def getList(n):
	freqFile = "word_freq.csv"
	wordlist = []
	with open(freqFile, 'rU') as readfile:
		reader = csv.reader(readfile)
		for row in reader:
			for word in row:
				if "+" in word:
					wordlist.extend(word.split("+"))
				else:
					word.append(word)

	return wordlist
