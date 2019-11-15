# Write a Python program to sum all the numeric items in a list?



array =  [1,5,8,'a','apple','d']
result = 0 
for a in array:
	if not(isinstance(a, str)):
		result = result + a

print(result)



