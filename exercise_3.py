data = """
CHÍNH CHỦ - BÁN NHÀ 2 MẶT TIỀN ĐƯỜNG 25, PHƯỜNG 10, QUẬN 6
Do không có nhu cầu sử dụng nữa tôi cần bán lại căn nhà 3 mặt tiền
Diện tích: 105.5 m2 (4.5 x 20m) nở hậu 6.8m, diện tích sàn: 283.8m2. Hướng Đông
Giá bán: 14.5 tỷ - liên hệ chính chủ: gặp A Phương
"""

# Tìm chiều dài và chiều rộng và giá bán.
if __name__ == '__main__':
    data = data.split(":")
    chieu_rong = data[1][11:14]
    chieu_dai = data[1][16:19]
    gia = data[3][0:5]
    print(chieu_rong, chieu_dai, gia)