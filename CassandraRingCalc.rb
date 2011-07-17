/*
Copyright 2011, Buddy Chell

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Takes as argument the number of nodes in your cluster and returns
the token ranges you can use on each of your nodes to balance.

You can read more here:
http://wiki.apache.org/cassandra/Operations#Load_balancing
*/

// CassandraRingCalc.rb

$num = 0;
if ARGV.length > 0 && (Integer(ARGV[0]) rescue false)
	$num = Integer(ARGV[0])
else
	puts "Node count must be a number greater than 0"
	Process.exit
end
0.upto($num-1) { |i| puts "Node: #{i} initial_token: #{(2**127)*i/$num}" }