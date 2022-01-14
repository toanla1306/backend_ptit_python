import re


if __name__ == '__main__':

	data = """
		CHÍNH CHỦ - BÁN NHÀ 2 MẶT TIỀN ĐƯỜNG 25, PHƯỜNG 10, QUẬN 6
		Do không có nhu cầu sử dụng nữa tôi cần bán lại căn nhà 3 mặt tiền
		Diện tích: 105.5 m2 (4.5 x 20m) nở hậu 6.8m, diện tích sàn: 283.8m2. Hướng Đông
		Giá bán: 14.5 tỷ - liên hệ chính chủ: gặp A Phương
	    """

	# str = 'Học lập trình Toidicode.com'
	matc = re.findall('\d+.\d+ . \d+', data)
	gia = re.findall('\d+.\d+ ', data)
	if matc:  # nếu tồn tại  chuỗi khớp
		print("chieu rong chieu dai la")
		print(matc)  # in ra chuỗi đó
	else:
		print('Khong tim thay!')  # Không thì hiện thông báo
	if gia:  # nếu tồn tại  chuỗi khớp
		print(gia)  # in ra chuỗi đó
	else:
		print('Khong tim thay!')  # Không thì hiện thông báo
	gia = list(gia)
	print("gia:" ,gia[len(gia) - 1],"ty")

# Tìm chiều dài và chiều rộng và giá bán.