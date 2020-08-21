'''
Created on 16 Aug, 2020

@author: ABD
'''
largest = None
smallest = None
num = None
inp = None
while inp!='done' :
    try :
        inp = input("Enter a number: ")
        if inp=='done' :
            break
        num = int(inp)
        if largest==None :
            largest=num
        if smallest==None :
            smallest=num
        if largest<num :
            largest=num
        if smallest>num :
            smallest=num
    except :
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)