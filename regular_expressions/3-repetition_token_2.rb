#!/usr/bin/env ruby

# This script matches strings that start with 'h', followed by 'b',
# then zero or more 't's, and ending with 'n'.
puts ARGV[0].scan(/hbt*n/).join

