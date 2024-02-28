import random

def san_sinh_mang(n):
    mang = []

    for i in range(n):
        so_ngau_nhien = random.randint(0,100)
        mang.append(so_ngau_nhien)

    return mang

def sap_xep_noi_bot(mang):
    n = len(mang)

    for i in range(n):
        tiep_tuc = False
        for j in range(n - 2, i - 1, -1):
            if mang[j] > mang[j + 1]:
                mang[j], mang[j+1] = mang[j+1], mang[j]
                tiep_tuc = True
        print(i + 1, '-', mang)

        if tiep_tuc == False:
            break

def main():
    mang = san_sinh_mang(10)
    print("Mang ban dau: \n{}".format(mang))
    sap_xep_noi_bot(mang)
    print("Mang sau khi sap xep: \n{}".format(mang))


if __name__ == '__main__':
    main()
