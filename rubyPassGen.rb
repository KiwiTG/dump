require 'securerandom'

print "Enter Password Length |> "
len = gets

led = len.to_i / 2

puts "\nA/N > #{SecureRandom.alphanumeric(len.to_i)}"
puts "Hex > #{SecureRandom.hex(led)}"
puts "Base64 > #{SecureRandom.base64(led)}"
puts "URL_Base64 > #{SecureRandom.urlsafe_base64(led)}"
