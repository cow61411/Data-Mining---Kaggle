import sys

f = open(sys.argv[1] , 'r')
f2 = open(sys.argv[1] , 'r')
w = open("datatest.txt" , 'w')

product = []
time = []
customer = []
promotion = []
store = []
storesale = []
storecost = []
unit = []
attribute = []
first = True
content = f.readline()
i = 0
#attribute = content.split(',')
#for n in range(len(attribute)):
	#w.write(attribute[n])
	#if n != len(attribute) - 1:
		#w.write(",")
for temp in f.readlines():
	temp = temp.split(',')
	temp = map(str.strip , temp)
	judge = True
	for n in range(len(product)):
		if product[n] == temp[0]:
			judge = False
	if judge:
		product.append(temp[0])
	judge = True
	for n in range(len(time)):
		if time[n] == temp[1]:
			judge = False
	if judge:
		time.append(temp[1])
	judge = True
	for n in range(len(customer)):
		if customer[n] == temp[2]:
			judge = False
	if judge:
		customer.append(temp[2])
	judge = True
	for n in range(len(promotion)):
		if promotion[n] == temp[3]:
			judge = False
	if judge:
		promotion.append(temp[3])
	judge = True
	for n in range(len(store)):
		if store[n] == temp[4]:
			judge = False
	if judge:
		store.append(temp[4])
	judge = True
	for n in range(len(storesale)):
		if storesale[n] == temp[5]:
			judge = False
	if judge:
		storesale.append(temp[5])
	judge = True
	for n in range(len(storecost)):
		if storecost[n] == temp[6]:
			judge = False
	if judge:
		storecost.append(temp[6])
	judge = True
	for n in range(len(unit)):
		if unit[n] == temp[7]:
			judge = False
	if judge:
		unit.append(temp[7])
product.sort()
time.sort()
customer.sort()
promotion.sort()
store.sort()
storesale.sort()
storecost.sort()
unit.sort()

for n in range(len(product)):
	attribute.append("product_id=")
	attribute.append(product[n])
	attribute.append(",")
for n in range(len(time)):
	attribute.append("time_id=")
	attribute.append(time[n])
	attribute.append(",")
for n in range(len(customer)):
	attribute.append("customer_id=")
	attribute.append(customer[n])
	attribute.append(",")
for n in range(len(promotion)):
	attribute.append("promotion_id=")
	attribute.append(promotion[n])
	attribute.append(",")
for n in range(len(store)):
	attribute.append("store_id=")
	attribute.append(store[n])
	attribute.append(",")
for n in range(len(storesale)):
	attribute.append("store_sales=")
	attribute.append(storesale[n])
	attribute.append(",")
for n in range(len(storecost)):
	attribute.append("store_cost=")
	attribute.append(storecost[n])
	attribute.append(",")
for n in range(len(unit)):
	attribute.append("unit_sales=")
	attribute.append(unit[n])
	if n != len(unit)-1:
		attribute.append(",")
for n in range(len(attribute)):
	w.write(attribute[n])
w.write("\n")
temp = f2.readline()
for temp in f2.readlines():
	temp = temp.split(',')
	temp = map(str.strip , temp)
	#attribute = []
	del attribute[:]
	for n in range(len(product)):
		if temp[0] == product[n]:
			attribute.append("1")
		else:
			attribute.append("0")
		attribute.append(",")
	for n in range(len(time)):
		if temp[1] == time[n]:
			attribute.append("1")
		else:
			attribute.append("0")
		attribute.append(",")
	for n in range(len(customer)):
		if temp[2] == customer[n]:
			attribute.append("1")
		else:
			attribute.append("0")
		attribute.append(",")
	for n in range(len(promotion)):
		if temp[3] == promotion[n]:
			attribute.append("1")
		else:
			attribute.append("0")
		attribute.append(",")
	for n in range(len(store)):
		if temp[4] == store[n]:
			attribute.append("1")
		else:
			attribute.append("0")
		attribute.append(",")
	for n in range(len(storesale)):
		if temp[5] == storesale[n]:
			attribute.append("1")
		else:
			attribute.append("0")
		attribute.append(",")
	for n in range(len(storecost)):
		if temp[6] == storecost[n]:
			attribute.append("1")
		else:
			attribute.append("0")
		attribute.append(",")
	for n in range(len(unit)):
		if temp[7] == unit[n]:
			attribute.append("1")
		else:
			attribute.append("0")
		if n != len(unit)-1:
			attribute.append(",")
	for n in range(len(attribute)):
		w.write(attribute[n])
	w.write("\n")
f.close()
f2.close()
w.close()
