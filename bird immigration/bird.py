import math
import time
"""Unit Converter"""
#Welcome and variable setting
print ("Welcome to  Unit Converter")
print("Coversion list  are : Length,Temp, Volume  "  )

val=int(input("ENTER INPUT"))
unit_in=input("from : ")
unit_out=input("To  : ")

def convert_SI(val, unit_in, unit_out):
    SI = {'mm':0.001, 'cm':0.01, 'm':1.0, 'km':1000.}
    return val*SI[unit_in]/SI[unit_out]



r1=convert_SI(val, unit_in, unit_out)
print(r1)



