#!/usr/bin/env ruby  

# Get the argument passed to the script  
input_string = ARGV[0]  

# Regular expression based on the pattern analysis  
pattern = /^hbt+n$/  

if input_string =~ pattern  
  puts "Match"  
else  
  puts "No match"  
end