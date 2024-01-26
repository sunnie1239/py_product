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

# write file
with open('product.csv', 'w', encoding='utf-8') as f:
	f.write('Item 商品, Price 價格\n')
	for d in product:
		f.write(d[0] + ',' + d[1] + '\n')	