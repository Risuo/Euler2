# using regular expressions

import re 
import urllib2

file_url = 'https://projecteuler.net/project/resources/p089_roman.txt'
rows = urllib2.urlopen(file_url).read()
 
print "Project Euler 76 Solution =", \
  len(rows) - len(re.sub("DCCCC|LXXXX|VIIII|CCCC|XXXX|IIII", '  ', rows))
  # the above code replaces, in order of those options, the above character strings, with a clear string of length 2, 
  # which is the length of the appropriate most-efficient representation of the roman numeral strings 