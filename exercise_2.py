# 1. Đọc file sdt_nhan_vien.txt xác định số điện thoại nhập sai
# 2. Sửa lại số điện thoại bị sai, nếu số lớn hơn 10 thì bỏ chữ số cuối, và số có chữ cái thì bỏ chữ cái đi

def repair_number(number):
    num = number.split(":")
    if len(num[0]) <= 10:
        return num[0] + ':' + num[1]
    i = 0
    while len(num[0]) != 10:
        if i == 10:
            num[0] = num[0][:10]
            break
        if num[0][i] < '0' or num[0][i] > '9':
            num[0] = num[0].replace(num[0][i], '')
            continue
        i+=1
    return num[0] + ':' + num[1]

def check_number(number):
    num = repair_number(number)
    if len(num) != len(number):
        print("wrong number: " + number)
    return num

if __name__ == '__main__':
    f = open("sdt_nhan_vien.txt", "r")
    list_number = []
    for x in f:
        list_number.append(x)
    for i in range(len(list_number)):
        list_number[i] = check_number(list_number[i])
    print(list_number)
