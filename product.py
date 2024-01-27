import os

product = []

# check file exist or not
if os.path.isfile('product.csv'):
	print("There is product.csv file.")
	# read file
	with open('product.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if 'Item 商品, Price 價格' in line:
				continue # 執行下一次迴圈
			[name, price] = line.strip().split(',')
			product.append([name, price])
else:
	print("There's no product.csv file.")			

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