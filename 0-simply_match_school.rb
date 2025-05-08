#!/usr/bin/env ruby
# The script should take one argument

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

input_string = ARGV[0]

# Regular expression to match "School" exactly
regex = /School/

# Perform the match
match_result = input_string.match(regex)

# Print the result
if match_result
  puts "Match found: #{match_result.string}"
else
  puts "No match found."
end
