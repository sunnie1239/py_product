product = []

# enter new product
while True:
	name = input('Please enter product name: ')
	if name == 'q':
		break
	price = input('Please enter product price: ')	
	product.append([name, price])	

# print products on screen
for d in product:
	print('Name: ', d[0], 'Price: ', d[1])