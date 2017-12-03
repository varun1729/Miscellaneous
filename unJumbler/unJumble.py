import itertools
from nltk.corpus import wordnet
jumble = 'hardwork'
words = []
length = len (jumble)
for x in range (2,length):
	combGen = itertools.permutations(jumble,x)
	for comb in combGen:
		word = ''.join(comb)
		if (wordnet.synsets(word)):
			if (word not in words):
				words.append(word)
print (words)
print (len(words))