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

import argparse

rings = {}
useNTS = False
nodes = 0
datacenters = 0
output = 0
parser = None

def isEntry(f):
	if __name__ == "__main__":
		f()
	return f

def hash_line():
	print("#"*60)

def is_int(s):
	try: 
	  int(str(s))
	  return True
	except ValueError:
	  return False
	  
def error(message):
	print(">>>>ERROR: %s" % message)
	
def usage():
	parser.print_help()

def nts_tokens():
	initialTokens = list(map(lambda y: "%d" % ((2**127)*y/nodes), range(0,nodes)))
	if output > 0:
		if output <= datacenters:
			tokens = list(map(lambda t: int(t)+(output-1),initialTokens))
			hash_line()
			print("Data Center Ring", output)
			hash_line()
			single_ring_tokens(tokens)
		else:
			error("output arg is greater than number of datacenters")
			usage()
	else:
		increment = 0
		for d in range(datacenters):
			rings[d] = list(map(lambda t: int(t)+increment, initialTokens))
			increment += 1
			hash_line()
			print("Data Center Ring", d+1)
			hash_line()
			single_ring_tokens(rings[d])
				
def single_ring_tokens(_tokens=None):
	if _tokens is None:
		tokens = list(map(lambda y: "%d" % ((2**127)*y/nodes), range(0,nodes)))
	else:
		tokens = _tokens
	for n in range(nodes):
		print("Node:", n)
		print("\tinitial_token:", tokens[n])

def parse_args():
	global useNTS,nodes,datacenters,output
	args = parser.parse_args()
	useNTS = args.nts
	if is_int(args.nodes):
		nodes = int(args.nodes)
	if is_int(args.datacenters):
		datacenters = int(args.datacenters)
	if is_int(args.output):
		output = int(args.output)

# initialize script args
def args_init():
	global parser
	parser = argparse.ArgumentParser()
	parser.add_argument('-o', '--output',help='For NTS, output a specific datacenter.')
	parser.add_argument('-n', '--nodes',help='Sets the number of nodes on the ring.  If --nts is set it sets the number of nodes at each datacenter.')
	parser.add_argument('-d','--datacenters',help='Required for --nts.  Sets the number of datacenters to build overlapping rings for.')
	parser.add_argument('--nts', help='If set, generates multiple overlapping rings for NetworkTopologyStrategy. If not set, makes a single ring.', action='store_true')
	
@isEntry
def main():
	global useNTS,nodes,datacenters
	
	args_init()
	parse_args()
	
	#if nts flag is set, nodes and datacenters must be > 0
	if useNTS and nodes > 0 and datacenters > 0:
		nts_tokens()
		
	#if nts is not set, nodes flag must be > 0 and datacenters must be 0
	elif not useNTS and nodes > 0 and datacenters == 0:
		single_ring_tokens()
	else:
		error("not all required flags set")
		usage()
