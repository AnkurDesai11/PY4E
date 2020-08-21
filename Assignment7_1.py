'''
Created on 17 Aug, 2020

@author: ABD
'''
# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip()
    line = line.upper()
    print(line)
