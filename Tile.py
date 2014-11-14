from enum import Enum


class TileType(Enum):
	stone=1
	wood=2
	treasure=3
	monster=4
	ironOre=10
	dross=11
	iron=12
	silverOre=20
	pewter=21
	silver=22
	goldOre=30
	lead=31
	gold=32
	
	def __repr__(s):
		return s.name
		
class Tile:
	def __init__(s,v):
		if isinstance(v,int):
			s.type = TileType(v)
		else:
			s.type = TileType[v]
	
	def __repr__(s):
		return repr(s.type)


