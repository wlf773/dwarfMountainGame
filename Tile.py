


class Tile:
	
	def __init__(s,name):
		s.name=str(name)
		
	def __repr__(s):
		return s.name
	
		
		
thisTile=Tile("wood")
print(thisTile)