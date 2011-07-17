$i = 0;
$num = 0;
if ARGV.length > 0 && (Integer(ARGV[0]) rescue false)
	$num = Integer(ARGV[0])
else
	puts "Node count must be a number greater than 0"
	Process.exit
end
0.upto($num-1) { |i| puts "Node: #{i} initial_token: #{(2**127)*i/$num}" }