import itertools
from nltk.corpus import wordnet
jumble = 'cphuo'
words = []
length = len (jumble)
for x in range (3,length):
	combGen = itertools.permutations(jumble,x)
	for comb in combGen:
		word = ''.join(comb)
		if (wordnet.synsets(word)):
			if (word not in words):
				words.append(word)
		else:
			None




print (words)