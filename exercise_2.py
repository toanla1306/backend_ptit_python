# 1. Đọc file sdt_nhan_vien.txt xác định số điện thoại nhập sai
# 2. Sửa lại số điện thoại bị sai, nếu số lớn hơn 10 thì bỏ chữ số cuối, và số có chữ cái thì bỏ chữ cái đi

import re
data = open("sdt_nhan_vien.txt", "r").readlines()
data_repair = ''
for index in range(0,len(data)):
    data_employ = data[index].replace('\n', '').split(':')
    phone_number = data_employ[0]
    check_alpha_in_phone_number = re.findall('[a-z]+', phone_number)
    if len(phone_number) > 10:
        if len(check_alpha_in_phone_number) > 0:
            for alpha_in_phone_number in check_alpha_in_phone_number:
                phone_number = phone_number.replace(alpha_in_phone_number, '')
        else:
            phone_number = phone_number[:10]
        data_employ[0] = phone_number
    data_repair = data_repair + data_employ[0] + ':' + data_employ[1] + '\n'

file1 = open("sdt_nhan_vien.txt","w")
file1.write(data_repair)