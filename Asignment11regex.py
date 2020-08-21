'''
Created on 21 Aug, 2020

@author: ABD
'''
import re
name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_42.txt"
handle = open(name)
numsum = 0
for line in handle:
    line_num = re.findall('[0-9]+', line)
    for nums in line_num:
        num = float(nums)
        numsum = numsum + num
print(int(numsum))