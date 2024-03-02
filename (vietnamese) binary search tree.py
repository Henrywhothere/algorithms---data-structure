class Nut:
    def __init__(self, khoa=None):
        self.khoa = khoa
        self.trai = None
        self.phai = None

    def chen(self,khoa):
        if self is None:
            nut = Nut(khoa)
            self = nut
            return


        if khoa < self.khoa:
            if self.trai == None:
                self.trai = Nut(khoa)
            else:
                self.trai.chen(khoa)
        elif khoa > self.khoa:
            if self.phai == None:
                self.phai = Nut(khoa)
            else:
                self.phai.chen(khoa)
        else:
            print("Bi trung khoa {}".format(khoa))



class CayNhiPhan:
    def __init__(self, khoa=None):
        if khoa == None:
            self.goc = None
        else:
            self.goc = Nut(khoa)

    def chen(self, khoa):
        if self.goc == None:
            self.goc = Nut(khoa)
        else:
            self.goc.chen(khoa)

    def xoa(self, khoa):
        nut_cha = None
        cha_con = None
        nut_ht = self.goc

        while nut_ht != None:
            if nut_ht.khoa > khoa:
                nut_cha = nut_ht
                nut_ht = nut_ht.trai
                cha_con = 'trai'
            elif nut_ht.khoa < khoa:
                nut_ht = nut_ht.phai
                cha_con = 'phai'
            else:
                if nut_cha == None:
                    if nut_ht.trai == None and nut_ht.phai == None:
                        self.goc = None
                    elif nut_ht.trai == None:
                        self.goc = nut_ht.phai
                    elif nut_ht.phai == None:
                        self.goc = nut_ht.trai
                    else:
                        self.goc = nut_ht.phai
                        tam = self.goc
                        while tam.trai != None:
                            tam = tam.trai
                        tam.trai = nut_ht.trai
                elif nut_ht.trai == None and nut_ht.phai == None:
                    if cha_con == 'trai':
                        nut_cha.trai = None
                    else:
                        nut_cha.phai = None
                elif nut_ht.trai == None:
                    if cha_con == 'trai':
                        nut_cha.trai = nut_ht.phai
                    else:
                        nut_cha.phai = nut_ht.phai
                elif nut_ht.phai == None:
                    if cha_con == 'trai':
                        nut_cha.trai = nut_ht.trai
                    else:
                        nut_cha.phai = nut_ht.trai
                else:
                    if cha_con == 'trai':
                        nut_cha.trai = nut_ht.phai
                    else:
                        nut_cha.phai = nut_ht.phai

                    if nut_ht.phai.trai == None:
                        nut_ht.phai.trai = nut_ht.trai
                    else:
                        tam = nut_ht.phai
                        while tam.trai != None:
                            tam = tam.trai
                        tam.trai = nut_ht.trai
                del nut_ht
                break
                        
                    


    def duyet_trai_nut_phai(self, goc=0):
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc

        if nut_ht == None:
            return []
        else:
            kq = []

        

            kq_trai = self.duyet_trai_nut_phai(nut_ht.trai)
            for x in kq_trai:
                kq.append(x)


            kq.append(nut_ht.khoa)
            
            
            kq_phai = self.duyet_trai_nut_phai(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)

            return kq


    
    def duyet_nut_trai_phai(self, goc=0):
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc

        if nut_ht == None:
            return []
        else:
            kq = []

            kq.append(nut_ht.khoa)


            kq_trai = self.duyet_nut_trai_phai(nut_ht.trai)
            for x in kq_trai:
                kq.append(x)
            
            kq_phai = self.duyet_nut_trai_phai(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)

            return kq


    def duyet_trai_phai_nut(self, goc=0):
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc

        if nut_ht == None:
            return []
        else:
            kq = []

            


            kq_trai = self.duyet_trai_phai_nut(nut_ht.trai)
            for x in kq_trai:
                kq.append(x)
            
            kq_phai = self.duyet_trai_phai_nut(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)


            kq.append(nut_ht.khoa)

            return kq

    
    def tim(self, khoa):
        if self.goc == None:
            return

        nut_ht = self.goc
        kq = ''
        while(nut_ht != None and nut_ht.khoa != khoa):
            kq = kq + f'{nut_ht.khoa} -> '
            if khoa <= nut_ht.khoa:
                nut_ht = nut_ht.trai
            else:
                nut_ht = nut_ht.phai

        if nut_ht == None:
            return None
        else:
            kq = kq + f'{nut_ht.khoa}'
            return kq

def main():
    so_phan_tu = 10
    cay = CayNhiPhan()

    print("+++ Chen vao cay +++")

    tap_gia_tri = set()
    from random import randint
    while len(tap_gia_tri) < so_phan_tu:
        gt = randint(1, 100)
        tap_gia_tri.add(gt)

    tap_gia_tri = list(tap_gia_tri)
    print('Chen lan luot', tap_gia_tri)
    for x in tap_gia_tri:
        cay.chen(x)

    kq = cay.duyet_trai_nut_phai()
    print("++++ Duyet cay theo trai-nut-phai: ",kq)

    kq = cay.duyet_nut_trai_phai()
    print("++++ Duyet cay theo nut-trai-phai: ",kq)


    kq = cay.duyet_trai_phai_nut()
    print("++++ Duyet cay theo trai-phai-nut: ", kq)


    gt = int(input("Nhap so can xoa: "))
    print("Xoa {}".format(gt))
    cay.xoa(gt)


    
    while True:
        nhap = input('Nhap vao khoa can tim: ')
        if nhap == '':
            break

        gt = int(nhap)
        kq = cay.tim(gt)
        if kq == None:
            print("Không tìm thấy {}".format(gt))
        else:
            print("tìm thấy {}: {}".format(gt, kq))

if __name__ == '__main__':
    main()

    









            
