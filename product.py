import os

# read file
def read_file(filename):
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if 'Item 商品, Price 價格' in line:
				continue # 執行下一次迴圈
			[name, price] = line.strip().split(',')
			product.append([name, price])
	return product		
						

# enter new product
def user_input(product):
	while True:
		name = input('Please enter product name: ')
		if name == 'q':
			break
		price = input('Please enter product price: ')	
		product.append([name, price])
	return product	


# print products
def print_product(product):
	for d in product:
		print('Name: ', d[0], 'Price: ', d[1])


# write file
def write_file(filename, product):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('Item 商品, Price 價格\n')
		for d in product:
			f.write(d[0] + ',' + d[1] + '\n')


filename = 'product.csv'
product = []
# check file exist or not
if os.path.isfile(filename):	
	product = read_file(filename)
else:
	print('Cannot find the file!')	
product = user_input(product)
print_product(product)
write_file(filename, product)	