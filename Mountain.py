from random import shuffle
from Tile import Tile

MROWS=5
MCOLS=5

class Mountain:
	d = []
	
	def __init__(s):
		for i in range(MROWS):
			temp = []
			for j in range(MCOLS):
				temp.append(MountainDeck(i,j))
			s.d.append(temp)
	
	def pp(s):
		for i in range(MROWS):
			print(repr(s.d[i]))
			

class MountainDeck:
	deck = ["String1"]
	
	def __init__(s,i,j):
		s.deck = [str(i)+str(j)]
		
	def __repr__(s):
		return s.deck[0]
		

def Test():			
	m = Mountain()
	m.pp()
	
Test()