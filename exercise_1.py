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

def tim_min(a1,a2,a3):
	min_1 = a1
	t = 1
	if min_1 > a2:
		min_1 = a2
		t = 2
		if min_1 > a3:
			min_1 = a3
			t = 3
	else:
		if min_1 > a3:
			min_1 = a3
			t = 3
	return t
# Tìm product_1 và product_2 ở cửa hàng nào có mức giá tốt nhất, dữ liệu trả về
# data_return = {"product_1":"store_2", "product_2":"store_3"}
if __name__ == '__main__':
	print(data["store_1"][0]["product_1"]["price"])
	a1=data["store_1"][0]["product_1"]["price"]
	a2=data["store_2"][0]["product_1"]["price"]
	a3=data["store_3"][0]["product_1"]["price"]
	a=tim_min(a1,a2,a3)

	a= "store_{}".format(str(a))
	b1=data["store_1"][1]["product_2"]["price"]
	b2=data["store_2"][1]["product_2"]["price"]
	b3=data["store_3"][1]["product_2"]["price"]
	b=tim_min(b1,b2,b3)
	b="store_{}".format(b)
	data_return={"product_1":a, "product_2":b}
	print(data_return)

