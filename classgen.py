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

import sys,getopt,os

#Writes out standard apache license header
def write_header():
	s = '''
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
'''
	return s
#writes out class name based on the -c or --class argument
def create_class(c):
	return '''
class %s:''' % c

#writes out method for each argument for the -m or --methods command
#adds self as default first parameter if none are specified
def create_method(m):
	method = '%s(self)' % m
	if '()' in m or '(' in m or ')' in m:
		method = m
	s = '''
	def %s:
		pass''' % (method)
	return s

#entry point
def main():
	filename = "newclass"
	if os.name in ['posix', 'os2']:
		path = './'
	else:
		path = '.\\'
	methods = []
	overwrite = False
	classname = '***EMPTY***'
	includeHeader = False
	opts, args = getopt.getopt(sys.argv[1:], "p:f:c:m:oh", ["path=","filename=","class=","overwrite","header","methods="])
	for opt, arg in opts:
		if opt in ['-h','--header']:
			includeHeader = True
		if opt in ['--methods','-m']:
			#multiple methods can be passed in delimited by commas
			for a in arg.split('/'):
				#methods that require parameters can be added delimited by @ symbol
				# example:
				#	-m init,__str__,my_method(self@x@y='test')
				#methods.append(a.replace('.',','))
				methods.append(a)
		if opt in ['--filename','-f']:
			filename = arg
		if opt in ['-o','--overwrite']:
			#print("OVERWRITE")
			overwrite = True
		if opt in ['-c','--class']:
			classname = arg
		if opt in ['-p', '--path']:
			path = arg
	filename = '%s/%s.py' % (path,filename)
	if not os.path.exists(filename) or overwrite:
		#print("WRITING....")
		file = open(filename,'w')
		file.write("#!/usr/bin/python")
		if includeHeader:
			file.write(write_header())
		file.write(create_class(classname))
		for s in methods:
			file.write(create_method(s))
		file.close()
	else:
		print("FILE EXISTS")
		sys.exit()
main()