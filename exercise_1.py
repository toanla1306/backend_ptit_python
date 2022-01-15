data = {
	"store_1": [
		{
			"product_1":{"price":"2500", "detail":"abcd"}
		},
		{
			"product_2":{"price":"4000", "detail":"qwert"}
		}
	],
	"store_2": [
		{
			"product_1":{"price":"1400", "detail":"abcd"}
		},
		{
			"product_2":{"price":"3800", "detail":"qwert"}
		}
	],
	"store_3": [
		{
			"product_1":{"price":"1500", "detail":"abcd"}
		},
		{
			"product_2":{"price":"3500", "detail":"qwert"}
		}
	]
}


# Tìm product_1 và product_2 ở cửa hàng nào có mức giá tốt nhất, dữ liệu trả về
# data_return = {"product_1":"store_2", "product_2":"store_3"}
def min_price(data, store, type_product, min_price):
	if len(min_price) == 0:
		min_price[store] = int(data[type_product]['price'])
	elif int(list(min_price.values())[0]) > int(data[type_product]['price']):
		min_price = {}
		min_price[store] = int(data[type_product]['price'])
	return min_price

if __name__ == '__main__':
	min_price_product_1 = {}
	min_price_product_2 = {}
	data_return = {}
	for store, products in data.items():
		for product in products: 
			try:
				min_price_product_1 = min_price(product, store, 'product_1', min_price_product_1)
			except:
				min_price_product_2 = min_price(product, store, 'product_2', min_price_product_2)

	data_return['product_1'] = list(min_price_product_1.keys())[0]
	data_return['product_2'] = list(min_price_product_2.keys())[0]
	print(data_return)
