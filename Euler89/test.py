import urllib2


f = urllib2.urlopen('http://www.python.org/')
rows = f.read()
print rows