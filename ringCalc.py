import sys
rings = {}
def Break():
	#print("------------------------------------------------------------")
	print("#########################################################")
def IsInt(s):
	try: 
	  int(s)
	  return True
	except ValueError:
	  return False
def CalculateTokens(nodesPerRing):
	n = list(map(lambda y: "%d" % ((2**127)*y/nodesPerRing), range(0,nodesPerRing)))
	increment = 0
	for x in range(nodesPerRing):
		rings[x] = list(map(lambda t: int(t)+increment, n))
		increment += 1
	for r in range(nodesPerRing):
		ringCount = 1
		Break()
		print("Ring", r)
		Break()
		for v in rings[r]:
			print("Token", ringCount, ":",v)
			ringCount += 1
		#Break()
if len(sys.argv) > 1:
	nodes = sys.argv[1]
	while not IsInt(nodes):
		print("Must enter a valid number of nodes")
		nodes = input()
	#Break()
	CalculateTokens(int(nodes))