import time
import fluidsynth

tabFile = open("tab.txt", "r+")
array = [ ]
for line in tabFile:
	row = []
	count = 0
	for x in range (0,len(line)):
		if (line[x] != '\n'):
			row.append(line[x])
	array.append(row)

def fixArray (array):
	for row in array:
		for x in range (0, len(row) - 2):
			if (row[x] != '-' and row[x] != '|'):
				if (row[x+1] != '-' and row[x+1] != '|'): 
					row[x] = row[x] + row[x+1]
					row[x+1] = '-'
	return array


array = fixArray(array)



notes = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']

rowToOctave = {0:'E4',1:'B3',2:'G3',3:'D3',4:'A2',5:'E2'}

def getOctave (ob, base, num):
	octave = int(ob)
	crit = 3
	relLoc = base + num
	if (relLoc < crit):
		return octave
	elif (base > crit and relLoc < 12):
		return octave
	elif (base < crit and relLoc < 12 and relLoc >=crit):
		return octave + 1
	else:
		diff = 12-base
		if (num - diff >= 3):
			return octave + 1
		else:
			return octave

def getNote (key,num,notes,row):
	octave = rowToOctave[row] [1:]
	circle = len(notes)-1
	base = 0
	for x in range (0,circle):
		if (notes[x] == key):
			base = x
	val = base + num
	if (val > circle):
		while (val > circle):
			val = val-circle-1
		octave = getOctave(octave,base,num)
		note = str(notes[val]) + str(octave)
		return note
	else:
		octave = getOctave(octave,base,num)
		note = str(notes[val]) + str(octave)
		return note

maxCol = len(array[0])
maxRow = 6

tabLoc1 = []
tab = []
for x in range (2,maxCol):
	for y in range (0,maxRow):
		if(array [y] [x] != '-' and array [y] [x] != '|'):
			num = int(array[y][x])
			key = array [y] [0]
			note = getNote (key,num,notes,y)
			tab.append(note)
			tabLoc1.append([note, x, y])
#print tabLoc1
print tab
print (' '.join(tab))
tabFile.close()

def alphabeticalToMidiNote (musical):
	note = musical [:-1]
	octave = int(musical[len(musical)-1]) - 1
	convert =  {'C' :0 , 'C#':1 , 'D' :2 , 'D#':3 , 'E' :4 , 'F' :5 , 'F#':6 , 'G' :7 , 'G#':8 , 'A' :9 , 'B#':10, 'B' :11}
	return convert[note] + 12*octave


def getPause (tabLoc, pause):
	length = len (tabLoc)
	for x in range (0, length - 1):
		factor = tabLoc[x+1][1] - tabLoc[x][1]
		(tabLoc[x]).append(factor*pause)
	tabLoc[length -1].append(pause)
	return tabLoc

tabLoc1 = getPause(tabLoc1, 0.070)
#fluidsynth
fs = fluidsynth.Synth()
fs.start()

sfid = fs.sfload("Stratocaster VS.sf2")
fs.program_select(0, sfid, 0, 0)
'''
fs.noteon(0, 12, 120)
fs.noteon(0, 24, 120)
fs.noteon(0, 36, 120)

time.sleep(10.0)

fs.noteoff(0, 12)
fs.noteoff(0, 24)
fs.noteoff(0, 36)

time.sleep(10.0)
'''
print alphabeticalToMidiNote("C5")
for noteInfo in tabLoc1:
	note = noteInfo[0]
	pause = noteInfo[3]
	fs.noteon(0,alphabeticalToMidiNote(note),107)
	time.sleep(pause)

fs.delete()
