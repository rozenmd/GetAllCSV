import os
import urllib
import urllib2

DOWNLOADS_DIR = '/Volumes/Macintosh HD/Dropbox/Projects/Javascript/d3/maxrozen.com/PyGetCSV/downloaded'

# For every line in the file
input_file = open(‘urls.txt’, 'r')
count_lines = 0
for line in input_file:
    print line
    url = line.rsplit(',', 1)[-1]
    name = line[0:6]+'.csv'
    filename = os.path.join(DOWNLOADS_DIR, name)
    if not os.path.isfile(filename):
    	urllib.urlretrieve(url, filename)
    count_lines += 1
print 'number of lines:', count_lines