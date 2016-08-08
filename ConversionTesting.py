import baseConversionCore

print("Please input first a number, then a desired base. The output will be that number in your desired base")
number = int(input("The first number!"))
baseNew = int(input("What base would you like that in?"))

print(baseConversionCore.toNewBase(number, baseNew))

