
if __name__ == '__main__':
    data = """
    CHÍNH CHỦ - BÁN NHÀ 2 MẶT TIỀN ĐƯỜNG 25, PHƯỜNG 10, QUẬN 6
    Do không có nhu cầu sử dụng nữa tôi cần bán lại căn nhà 3 mặt tiền
    Diện tích: 105.5 m2 (4.5 x 20m) nở hậu 6.8m, diện tích sàn: 283.8m2. Hướng Đông
    Giá bán: 14.5 tỷ - liên hệ chính chủ: gặp A Phương
    """

    a=int(data.index("("))
    b=int(data.index("x"))
    c=int(data.index(")"))
    d=int(data.index("bán:"))
    print(data[a+1:b])
    print(data[b+2:c-1])
    print(data[d+5:d+10])

# Tìm chiều dài và chiều rộng và giá bán.