#!/usr/bin/python
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements. See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership. The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import sys,getopt,platform

rings = {}
useNTS = False
nodes = 0
datacenters = 0
output = 0

def hash_line():
	print("#"*60)

def is_int(s):
	try: 
	  int(s)
	  return True
	except ValueError:
	  return False
	
def usage():
	print(
'''--nts
  If set, generates multiple overlapping rings for
	NetworkTopologyStrategy.
  If not set, makes a single ring.

-n or --nodes
  Sets the number of nodes on the ring.  If --nts is set it sets the
  number of nodes at each datacenter.

-d or --datacenters
  Required for --nts.  Sets the number of datacenters to build
  overlapping rings for.

-o or --output
  For NTS, output a specific datacenter.
	Example:
  --------

  # A single ring with 10 nodes.
  ./ringCalc.py -n 10

  # 2 overlapping NTS style rings with four nodes.
  ./ringCalc.py --nts -n 4 -d 2 

  # 3 overlapping NTS style rings with 8 nodes, show only datacenter 3.
  ./ringCalc.py --nts -n 8 -d 3 -o 3'''
)
	sys.exit()
	
def error(message):
	print(">>>>ERROR: %s" % message)
	
def nts_tokens():
	initialTokens = list(map(lambda y: "%d" % ((2**127)*y/nodes), range(0,nodes)))
	if output > 0:
		if output <= datacenters:
			tokens = list(map(lambda t: int(t)+(output-1),initialTokens))
			hash_line()
			print("Data Center Ring", output)
			hash_line()
			for n in range(nodes):
				print("Node:", n)
				print("\tinitial_token:", tokens[n])
		else:
			error("output arg is greater than number of datacenters")
			usage()
	else:
		increment = 0
		for d in range(datacenters):
			rings[d] = list(map(lambda t: int(t)+increment, initialTokens))
			increment += 1
			ringCount = 0
			hash_line()
			print("Data Center Ring", d+1)
			hash_line()
			for v in rings[d]:
				print("Node", str(ringCount) + ":")
				print("\tinitial_token"+":",v)
				ringCount += 1
				
def single_ring_tokens():
	tokens = list(map(lambda y: "%d" % ((2**127)*y/nodes), range(0,nodes)))
	for n in range(nodes):
		print("Node:", n)
		print("\tinitial_token:", tokens[n])
		
def main(argv):
	global useNTS,nodes,datacenters,output
	if not argv:
		usage()
	try:
		opts, args = getopt.getopt(argv, "d:o:n:", ["help","nts","nodes=","datacenters=","output="])
	except getopt.GetoptError as e:
		error(e)
		usage()
	for opt, arg in opts:
		if opt == "--nts":
			useNTS = True
		elif opt == "--help":
			usage()
		elif opt in ["-n","--nodes"]:
			if is_int(arg):
				nodes = int(arg)
			else:
				usage()
		elif opt in ["-d","--datacenters"]:
			if is_int(arg):
				datacenters = int(arg)
			else:
				usage()
		elif opt in ["-o","--output"]:
			if is_int(arg):
				output = int(arg)
			else:
				usage()
	#if nts flag is set, nodes and datacenters must be > 0
	if useNTS and nodes > 0 and datacenters > 0:
		nts_tokens()
	#if nts is not set, nodes flag must be > 0 and datacenters must be 0
	elif not useNTS and nodes > 0 and datacenters == 0:
		single_ring_tokens()
	else:
		error("not all required flags set")
		usage()
		
		
if __name__ == "__main__":
    main(sys.argv[1:])
