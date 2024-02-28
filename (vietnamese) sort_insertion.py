import random

def san_sinh_so(n):
    mang = []

    for i in range(n):
        so_ngau_nhien = random.randint(0, 100)
        mang.append(so_ngau_nhien)

    return mang


def sap_xep_chen(mang):
    n = len(mang)

    for i in range(1, n):
        tam = mang[i]
        j = i
        while j > 0 and mang[j - 1] > tam:
            mang[j] = mang[j-1]
            j = j - 1

        mang[j] = tam
    return mang


def main():
    mang = san_sinh_so(10)
    print("Mang ban dau la: \n{}".format(mang))
    sap_xep_chen(mang)
    print("Mang sau khi sap xep la: \n{}".format(mang))

if __name__ == "__main__":
          main()
