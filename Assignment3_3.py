'''
Created on 14 Aug, 2020

@author: ABD
'''
score = input("Enter Score: ")

try :
    scr = float(score)
except :
    print("Please enter numeric value")
    quit()
    
if scr<=1.0 and scr>=0.9 :
    print("A")
elif scr<=1.0 and scr>=0.8 :
    print("B")
elif scr<=1.0 and scr>=0.7 :
    print("C")
elif scr<=1.0 and scr>=0.6 :
    print("D")
elif scr<=0.6 and scr>=0.0 :
    print("E")
else :
    print("Please enter value in 0-1 range")
quit()