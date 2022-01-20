import re

data = """
CHÍNH CHỦ - BÁN NHÀ 2 MẶT TIỀN ĐƯỜNG 25, PHƯỜNG 10, QUẬN 6
Do không có nhu cầu sử dụng nữa tôi cần bán lại căn nhà 3 mặt tiền
Diện tích: 105.5 m2 (4.5 x 20m) nở hậu 6.8m, diện tích sàn: 283.8m2. Hướng Đông
Giá bán: 14.5 tỷ - liên hệ chính chủ: gặp A Phương
"""
txt = "Diện tích: 105.5 m2 (4.5 x 20m) nở hậu 6.8m, diện tích sàn: 283.8m2. Hướng Đông"


# Tìm chiều dài và chiều rộng và giá bán.
if __name__ == '__main__':
    result1 = re.findall(":.*-", data)
    result2 = data[data.find('(') + 1:data.find('m)')]

    price = result1[0][2:(len(result1[0])-2)]
    width = result2.split("x")[0]
    heigh = result2.split("x")[1]
    print(price)
    print(width)
    print(heigh)