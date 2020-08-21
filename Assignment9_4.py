'''
Created on 19 Aug, 2020

@author: ABD
'''
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
names = dict()
highcount = None
highname = None
for line in handle:
    if line.startswith("From ") :
        linelist = line.split()
        names[linelist[1]] = names.get(linelist[1], 0) + 1
        if highname is None :
            highcount = names[linelist[1]]
            highname = linelist[1]
        if highcount < names[linelist[1]] :
            highcount = names[linelist[1]]
            highname = linelist[1]
print(highname, highcount)