# 1. Đọc file sdt_nhan_vien.txt xác định số điện thoại nhập sai
# 2. Sửa lại số điện thoại bị sai, nếu số lớn hơn 10 thì bỏ chữ số cuối, và số có chữ cái thì bỏ chữ cái đi
if __name__ == '__main__':
    f = open("sdt_nhan_vien.txt", encoding='UTF-8')

    doc=f.read()
    b=doc.split("\n")

    for i in range(len(b)):
        j = 0
        while j <= len(b[i]):
            if b[i][j] == ":":
                if j == 11:
                    b[i] = b[i].replace(b[i][j-1], "")
                break
            else :
                if b[i][j] < "0" or b[i][j] > "9":
                    b[i]=b[i].replace(b[i][j] ,"")
                    print(b[i])
                else :
                    j=j+1
    print(b)

