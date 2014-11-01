

class Card:

	def __init__(s,name,clan,text):
		s.name,s.clan,s.text = name,clan,text
	
	def __repr__(s):
		return("Card name is: "+s.name+", clan is: "+s.clan)	
		
		
		
		
card = Card("Prospector","Mining Guild","Text goes here")
print(card)

