import os #operating system

#讀取檔案
def read_file(filename):
    products = []
    with open(filename,'r' ) as f: #encoding='utf-8'
        for line in f:
            if'商品,價格' in line:
                continue #繼續 跳到下一回
            name, price = line.strip().split(',')#strip去調換行符號 split切割 
            products.append([name, price])
    return products

#讓使用者輸入
def user_input(products):
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
    return products

#印出所有購買紀錄
def print_products(products):
    for product in products:
        print(product[0], '的價格是', product[1])

#寫入檔案
def write_file(filename, products):
    with open(filename, 'w') as f: #r讀取 w寫入
        f.write('商品,價格\n')
        for product in products:
            f.write(product[0] + ',' + str(product[1]) + '\n')
            #open只是打開而已 下面的write才是真的寫入

def main():#將此段執行程式包裹成一個主要執行程式碼
    filename = 'product.csv'
    if os.path.isfile(filename): #檢查檔案是否有在此路徑裡
        print('YA! 找到檔案')
        products = read_file(filename)
    else:
        print("找不到檔案....")

    products = user_input(products)
    print_products(products)
    write_file('product.csv', products)

main()