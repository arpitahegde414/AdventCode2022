import re
my file = open("Day4Input.txt")
data = my_file.read()
data_to_list = data.split("\n")
count = 0
for i in data_to_list:
	l = re.split(r'[,-)+',i)
	rangel = set(range(int(1[0]),int(1[i])+1))
	range2 set (range (int (1[2]) ,int(1[3])+1))
	common = list(rangel.intersection(range2))
	if len(common)>0:
		count+=1
print (count)
