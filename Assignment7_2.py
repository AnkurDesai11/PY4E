'''
Created on 17 Aug, 2020

@author: ABD
'''
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
average = 0
count = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") : 
        line = line.rstrip()
        strnum = line[20:]
        num = float(strnum)
        count = count + 1
        average = average + num
average = average/count
print('Average spam confidence:', average)