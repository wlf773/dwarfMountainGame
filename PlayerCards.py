from random import shuffle
from Card import Card
from Tile import Tile

class PlayerCards:
	deck = []
	hand = []
	discard = []
	board = [[None] * 5 for x in range(5)]
		
		
	def __init__(s,cardType):
		s.cardType=cardType
	

	def shuffleIntoDeck(s,cards):
		shuf = s.deck + cards
		shuffle(shuf)
		s.deck = shuf
		print("Shuffling "+str(shuf)+" into deck.")
		return []
		
	def draw(s,n=1):
		for i in range(n):
			
			#If deck is empty, shuffle in discard.
			if(len(s.deck)==0 and len(s.discard)!=0):
				s.discard = s.shuffleIntoDeck(s.discard)
				s.draw()
			#If deck is empty and discard is empty, no draw can be done.
			elif(len(s.deck)==0 and len(s.discard)==0):
				print("There are no more cards to draw.")
			#Draw the card.
			else:
				s.hand.append(s.deck.pop(0))
				
	def discardCards(s,cards,where):
		result=[]
		for card in cards:
			result.append(s.discardCard(card,where))
		for r in result:
			if r == False:
				return False
		return True
		
		
	def discardCard(s,card,where):
		if not isinstance( card, s.cardType):
			return s.discardCards(card,where)
		print("Trying to discard "+str(card)+" from "+str(where))
		if card in where:
			where.remove(card)
			s.discard.append(card)
			return True
		else:
			return False


	def pp(s):
		print("Hand:  "+str(s.hand))
		print("Deck:  "+str(s.deck))
		print("Discard:  "+str(s.discard))
		for i in range(5):
			print(str(s.board[i]))
		print()


def Test():
	p1 = PlayerCards(int)
	p1.deck = [i for i in range (10)]
	p1.discard = [i for i in range (10,20)]
	p1.pp()

	p1.draw(15)
	p1.pp()

	print(p1.discardCard([0],p1.hand))
	p1.pp()
	
	p1.board[2][1]=Tile("stone")
	p1.pp()


Test()

