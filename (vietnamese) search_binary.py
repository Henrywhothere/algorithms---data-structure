import random

def san_sinh_mang(n):
    mang = []
    so_dau_tien = random.randint(-100, 100)
    mang.append(so_dau_tien)

    for i in range(1, n):
        tang = random.randint(1, 10)
        so = mang[i-1] + tang
        mang.append(so)
    return mang


def tim_nhi_phan(mang, x):
    trai = 0
    phai = len(mang) - 1
    while trai <= phai:
        giua = (trai + phai)//2

        if mang[giua] == x:
            return giua
        elif x < mang[giua]:
            phai = giua - 1
        else:
            trai = giua + 1
    return -1


def main():
    mang = san_sinh_mang(20)
    print(mang)

    x = int(input("Nhap vao gia tri so nguyen can tim: "))

    vitri = tim_nhi_phan(mang,x)

    if vitri != -1:
        print("Gia tri {} duoc tim thay tai vi tri {}".format(x, vitri))
    else:
        print("khong tim thay gia tri")

if __name__ == "__main__":
    main()
