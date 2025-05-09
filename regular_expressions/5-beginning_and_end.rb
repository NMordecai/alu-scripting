#!/usr/bin/env ruby

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

input_string = ARGV[0]
regex = /h.n/

if input_string.match(regex)
  puts "Match found!"
else
  puts "No match found."
end
