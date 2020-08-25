'''
Created on 24 Aug, 2020

@author: ABD
Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_896975.xml (Sum ends with 37)
 The data consists of a number of names and comment counts in XML as follows:

<comment>
  <name>Matthias</name>
  <count>97</count>
</comment>

You are to look through all the <comment> tags 
and find the <count> values sum the numbers. 
To make the code a little simpler, 
you can use an XPath selector string to look through 
the entire tree of XML for any tag named 'count' with the following line of code:

counts = tree.findall('.//count')

Take a look at the Python ElementTree documentation and look for the supported XPath syntax for details. 
You could also work from the top of the XML down to the comments node and then loop through the child nodes of the comments node.
'''
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL- ')
#similar to 
#xml = urllib.request.urlopen(url, context=ctx)
#data = xml.read()
xml = urllib.request.urlopen(url, context=ctx).read()
#print('Retrieved', len(data), 'characters')
#print(data.decode())
numsum = 0
tree = ET.fromstring(xml)
counts = tree.findall('.//count')
for i in range(0, len(counts)) :
    num = float(counts[i].text)
    numsum = numsum + num
print(int(numsum))