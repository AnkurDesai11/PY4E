'''
Created on 23 Aug, 2020

@author: ABD

Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). 
Follow that link. 
Repeat this process 4 times. The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah
Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Kobi.html
Find the link at position 18 (the first name is 1). 
Follow that link. 
Repeat this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: D

'''
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL- ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
position = input('Enter link position -')
repitition = input('Enter number of repititions -')
try :
    pos = int(position)
    rep = int(repitition)
except :
    print("Enter numerical values")
tags = list()
for i in range(0, rep) :
    tags = soup('a')
    tag = tags[pos-1].get('href', None)
    html = urllib.request.urlopen(tag, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
nameurl = tags[pos-1].get('href', None)
name = re.findall('_([A-Za-z]+)\.', nameurl)
print(name)
