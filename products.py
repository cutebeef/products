products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')	
    #p = [ ]
    #p.append(name)  
    #p.append(price)
    #products.append(p)
	products.append([ name, price ])    
print(products)

for product in products:
	print(product[0], '的價格是', product[1])

with open('product.csv', 'w') as f: #r讀取 w寫入
	 for product in products:
	 	f.write(product[0] + ',' + product[1] + '\n')
	 	#open只是打開而已 下面的write才是真的寫入