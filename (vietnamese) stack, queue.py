class Nut:
    def __init__(self, gia_tri):
        self.gia_tri = gia_tri
        self.nut_ke_tiep = None



class DSLienKet:
    def __init__(self):
        self.dau = None
        self.duoi = None

    def __str__(self):
        kq = ''
        stt = 0
        hien_tai = self.dau
        while hien_tai != None:
            stt += 1
            if stt == 1:
                kq = kq + str(hien_tai.gia_tri)
            else:
                kq = kq + ' -> ' + str(hien_tai.gia_tri)
            hien_tai = hien_tai.nut_ke_tiep

        return kq

    def them_dau(self, gia_tri):
        nut = Nut(gia_tri)
        if self.dau == None:
            self.dau = nut
            self.duoi = nut
        else:
            nut.nut_ke_tiep = self.dau
            self.dau = nut

    def them_duoi(self, gia_tri):
        nut = Nut(gia_tri)
        if self.dau == None:
            self.dau = nut
            self.duoi = nut
        else:
            self.duoi.nut_ke_tiep = nut
            self.duoi = nut

    def lay_dau(self):
        if self.dau == None:
            return None
        else:
            return self.dau.gia_tri

    def xoa_dau(self):
        tam = self.dau
        if self.dau == self.duoi:
            self.dau = None
            self.duoi = None
        else:
            self.dau = self.dau.nut_ke_tiep
            
        del tam


class NganXep:
    def __init__(self):
        self.danh_sach = DSLienKet()

    def rong(self):
        return self.danh_sach.dau == None

    def __str__(self):
        kq = 'Ngan Xep ['
        kq = kq + str(self.danh_sach)
        kq = kq + ']'
        return kq 

    def day_vao(self, gia_tri):
        self.danh_sach.them_dau(gia_tri)

    def lay_ra(self):
        if self.rong():
            return None
        else:
            kq = self.danh_sach.lay_dau()
            self.danh_sach.xoa_dau()
            return kq

class HangDoi:
    def __init__(self):
        self.danh_sach = DSLienKet()

    def __str__(self):
        kq = 'Hang Doi ['
        kq = kq + str(self.danh_sach)
        kq = kq + ']'
        return kq

    def rong(self):
        return self.danh_sach.dau == None


    def xep_hang(self, gia_tri):
        #enqueue
        self.danh_sach.them_duoi(gia_tri)


    def ra_hang(self):
        #dequeue
        if self.rong():
            return None
        else:
            kq = self.danh_sach.lay_dau()
            self.danh_sach.xoa_dau()
            return kq
                


if __name__ == '__main__':
    print("BÀI TẬP NGĂN XẾP")
    ngan_xep = NganXep()
    print(ngan_xep)

    print('-----Day vao -----')
    for i in range(1, 6):
        print("Day vao {}".format(i))
        ngan_xep.day_vao(i)
        print(ngan_xep)

    print('-----Lay ra -----')
    while not ngan_xep.rong():
        gt = ngan_xep.lay_ra()
        print("Lay ra -> {}".format(gt))
        print(ngan_xep)

    print("\n")
    print("\n")

    print("BÀI TẬP HÀNG ĐỢI")
    hang_doi = HangDoi()
    print(hang_doi)

    print('------Xep hang -----')
    for x in range(1,6):
        print("Xep hang {}".format(x))
        hang_doi.xep_hang(x)
        print(hang_doi)

    print('------Ra hang ------')
    while not hang_doi.rong():
        gt = hang_doi.ra_hang()
        print("ra hang -> {}".format(gt))
        print(hang_doi)
        


    
