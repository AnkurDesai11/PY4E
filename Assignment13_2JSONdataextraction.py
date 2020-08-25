'''
Created on 25 Aug, 2020

@author: ABD
Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_896976.json (Sum ends with 62)
'''
import urllib.request, urllib.parse, urllib.error
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL- ')
data = urllib.request.urlopen(url, context=ctx).read()
info = json.loads(data)
#print(len(info["comments"]))
numsum = 0
for i in range( 0, len(info["comments"]) ) :
    num = float(info["comments"][i]["count"])
    numsum = numsum + num
print(int(numsum))