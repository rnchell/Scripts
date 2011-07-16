require "date"
#DEFINE ROOT DIRECTORY
$path = "C:/Nodes"
$baseFileName = "Nodes"
$i = 0;
$num = 0;
if ARGV.length > 0 && (Integer(ARGV[0]) rescue false)
	$num = Integer(ARGV[0])
else
	puts "Node count must be greater than 0"
	Process.exit
end
if !File.directory?($path)
	Dir::mkdir($path)
end
file = File.new("#{$path}/#{$baseFileName}#{DateTime.now.strftime("%m%d%Y_%I%M%p")}.txt", "w")
while $i < $num  do
   s =  "Node: #{$i} initial_token: #{(2**127)*$i/$num}"
   puts s
   file.syswrite(s+"\r\n")
   $i += 1
end
file.close