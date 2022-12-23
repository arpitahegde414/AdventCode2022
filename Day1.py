my_file = open("DaylCaloriesInput.txt")
data = my_file.read()

data_to_list = data.split("\n")
array=[]

current_calories=0

length=len (data_to_list)
for i, val in enumerate (data_to_ list):
	if val!="':
		current_calories+=int (val)
		if i<length-1 and data_to_list[it+1l]=—'':
			array.append(current_calories)
			current_calories=0

		elif i=length-1:
			array.append(current_calories)
array.sort()
print (array[len(array)-1])
print (array[len (array) -2])
print (array[len (array) -3])
