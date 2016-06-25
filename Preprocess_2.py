import sys

f = open(sys.argv[1] , 'r')
f2 = open(sys.argv[1] , 'r')
w = open("datatesti2.txt" , 'w')

product = []
time = []
customer = []
productattri = []
transpro = []
transpro = []
attribute = []
content = f.readline()
i = 0
for temp in f.readlines():
	temp = temp.split(',')
	temp = map(str.strip , temp)
	judge = True
	for n in range(len(productattri)):
		if productattri[n] == temp[0]:
			judge = False
	if judge:
		productattri.append(temp[0])
	product.append(temp[0])
	time.append(temp[1])
	customer.append(temp[2])
productattri.sort()

for n in range(len(productattri)):
	attribute.append(productattri[n])
	if n != len(productattri)-1:
		attribute.append(",")
for n in range(len(attribute)):
	w.write(attribute[n])
w.write("\n")

tempcus = []
temptime = []
n = 0

for n in range(len(customer)):
	judge = True
	for i in range(len(tempcus)):
		if tempcus[i] == customer[n] and temptime[i] == time[n]:
			judge = False
	if judge:
		tempcus.append(customer[n])
		temptime.append(time[n])


for n in range(len(tempcus)):
	del transpro[:]
	for i in range(len(customer)):
		if tempcus[n] == customer[i] and temptime[n] == time[i]:
			transpro.append(product[i])
	for j in range(len(productattri)):
		judge = False
		for k in range(len(transpro)):
			if transpro[k] == productattri[j]:
				judge = True
		if judge:
			w.write("1")
		else:
			w.write("0")
		if j != len(productattri) - 1:
			w.write(",")
	w.write("\n")
f.close()
f2.close()
w.close()
