#take input from the user
fnum = input('Enter the first number: ') 
snum = input('Enter the second number: ')

#Sum the Numbers
#result = ('fnum + snum')
#Output :
#Enter the first number:  34
#Enter the second number: 56
#3456
# Because the two number python consider is "string" 
#String is an universal data formate and this is becuase you can store another data formate in string.

#correction :
result = int(fnum) + int (snum)
print(result)
