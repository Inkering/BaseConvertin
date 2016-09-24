import base64
import math
import baseConversionCore

print("Please input first a number, then a desired base. The output will be that number in your desired base")
number = input("The first number!")
baseOld = int(input("What base is that in?"))
baseNew = int(input("What base would you like that in?"))

print(baseConversionCore.bases(number, baseOld, baseNew))

