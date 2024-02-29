import random

def san_sinh_mang(n):
    mang = []
    for i in range(n):
        so_ngau_nhien = random.randint(-100, 100)
        mang.append(so_ngau_nhien)
    return mang

def sap_xep_tron(mang):
    if len(mang) > 1:
        giua = len(mang) // 2
        mang_trai = mang[0:giua]
        mang_phai = mang[giua:]
        
        sap_xep_tron(mang_trai)
        sap_xep_tron(mang_phai)

        i = j = k = 0
        while i < len(mang_trai) and j < len(mang_phai):
            if mang_trai[i] < mang_phai[j]:
                mang[k] = mang_trai[i]
                i += 1
            else:
                mang[k] = mang_phai[j]
                j += 1
            k += 1

        while i < len(mang_trai):
            mang[k] = mang_trai[i]
            i += 1
            k += 1


        while j < len(mang_phai):
            mang[k] = mang_phai[j]
            j += 1
            k += 1
    


def main():
    mang = san_sinh_mang(10)
    print("Mang ban dau la: \n",mang)
    sap_xep_tron(mang)
    print("Mang sau khi sap xep: \n",mang)

if __name__ == '__main__':
    main()
                 

                
                
              
