###########################################
##### Single-Thread Ruby Port Scanner #####
###########################################

require 'socket'

TIMEOUT = 2
$port = 1

print "Enter Host IP > "
$host = gets.chomp
	
def scan_port()
	socket = Socket.new(:INET, :STREAM)
	remote_addr = Socket.sockaddr_in($port, $host)
	begin
		socket.connect_nonblock(remote_addr)
	rescue Errno::EINPROGRESS
	end
	_, sockets, _ = IO.select(nil, [socket], nil, TIMEOUT)
	if sockets
		puts "Port #{$port} is open"
	else
		puts "Port #{$port} is closed"
	end
	$port += 1
end

puts ""

while 1 < 2 do
	scan_port()
end
