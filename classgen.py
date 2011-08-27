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
def write_header():
	s = '''#!/usr/bin/python
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
def create_class(c):
	return '''
class %s:''' % c

def create_method(m):
	method = '%s(self)' % m
	if '()' in m or '(' in m or ')' in m:
		method = m
	s = '''
	def %s:
		pass''' % (method)
	return s

def main():
	title = "class"
	path = '.\\' #check for os?
	methods = []
	overwrite = False
	classname = 'class'
	opts, args = getopt.getopt(sys.argv[1:], "p:t:c:m:o", ["path=","title=","class=","overwrite","methods="])
	for opt, arg in opts:
		if opt in ['--methods','-m']:
			for a in arg.split(','):
				a = methods.append(a.replace('@',','))
				#create_class(a.replace('.',','))
		if opt in ['--title','-t']:
			title = arg
		if opt in ['-o','--overwrite']:
			#print("OVERWRITE")
			overwrite = True
		if opt in ['-c','--classes']:
			classname = arg
	filename = '%s/%s.py' % (path,title)
	if not os.path.exists(filename) or overwrite:
		#print("WRITING....")
		file = open(filename,'w')
		file.write(write_header())
		file.write(create_class(classname))
		for s in methods:
			file.write(create_method(s))
		file.close()
	else:
		print("FILE EXISTS")
		sys.exit()
main()