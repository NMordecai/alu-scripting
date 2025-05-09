#!/usr/bin/env ruby

# Get the first command-line argument
input = ARGV[0]

# Check if it matches the word "School"
puts input.scan(/School/).join
