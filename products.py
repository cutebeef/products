#讀取檔案
products = []
with open('product.csv','r') as f:
    for line in f:
        if'商品,價格' in line:
            continue #繼續 跳到下一回
        name, price = line.strip().split(',')#strip去調換行符號 split切割 
        products.append([name, price])
print(products)

#讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')	
	price = int(price)
    #p = [ ]
    #p.append(name)  
    #p.append(price)
    #products.append(p)
	products.append([ name, price ])    
print(products)

#印出所有購買紀錄
for product in products:
	print(product[0], '的價格是', product[1])
#寫入檔案
with open('product.csv', 'w') as f: #r讀取 w寫入
	 f.write('商品,價格\n')
	 for product in products:
	 	f.write(product[0] + ',' + str(product[1]) + '\n')
	 	#open只是打開而已 下面的write才是真的寫入