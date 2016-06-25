import sys

f = open(sys.argv[1] , 'r')
f2 = open(sys.argv[2] , 'r')
w = open("trans_and_cus.txt" , 'w')

product = []
time = []
customer = []
cusdata = []
cusid = []
attribute = []

content = f.readline()

i = 0
for temp in f.readlines():
	temp = temp.split(',')
	temp = map(str.strip , temp)
	product.append(temp[0])
	time.append(temp[1])
	customer.append(temp[2])

content = f2.readline()
for temp in f2.readlines():
	temp2 = temp
	temp = temp.split(',')
	temp = map(str.strip , temp)
	cusid.append(temp[0])
	cusdata.append(temp2)

attribute.append("product,")
attribute.append("time,")
attribute.append("customer,")
attribute.append(content)

for n in range(len(attribute)):
	w.write(attribute[n])
#w.write("\n")

for n in range(len(product)):
	del attribute[:]
	attribute = []
	attribute.append(product[n])
	attribute.append(",")
	attribute.append(time[n])
	attribute.append(",")
	attribute.append(customer[n])
	attribute.append(",")
	for m in range(len(cusid)):
		if customer[n] == cusid[m]:
			attribute.append(cusdata[m])
	for n in range(len(attribute)):
		w.write(attribute[n])
#w.write("\n")
