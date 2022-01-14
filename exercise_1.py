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
def get_price(x):
	price = []
	price.append(int(x[0]["product_1"]["price"]))
	price.append(int(x[1]["product_2"]["price"]))

	return price

def find_min_product(list_price):
	store = [0,0]

	product_1 = [x[0] for x in list_price]
	product_2 = [x[1] for x in list_price]

	min_value_1 = min(product_1)
	min_value_2 = min(product_2)
	store[0] = product_1.index(min_value_1) + 1
	store[1] = product_2.index(min_value_2) + 1

	return store

if __name__ == '__main__':
	list_price = []
	store = []
	for x in data:
		list_price.append(get_price(data[x]))

	store = find_min_product((list_price))
	data_return = {"product_1":f"store_{store[0]}", "product_2":f"store_{store[1]}"}
	print(data_return)
# Tìm product_1 và product_2 ở cửa hàng nào có mức giá tốt nhất, dữ liệu trả về

