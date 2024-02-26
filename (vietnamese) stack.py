class NganXep:
    def __init__(self):
        self.danh_sach = []



    def rong(self):
        return len(self.danh_sach) == 0


    def __str__(self):
        stt = 0
        kq = 'NganXep ['
        for x in self.danh_sach:
            stt += 1
            if stt == 1:
                kq = kq + str(x)
            else:
                kq = kq + ' -> ' + str(x)

        kq = kq + ']'
        return kq


    def day_vao(self, gia_tri):
        self.danh_sach.insert(0, gia_tri)

    def lay_ra(self):
        if self.rong():
            return None
        else:
            return self.danh_sach.pop(0)


if __name__ == '__main__':
    ngan_xep = NganXep()
    print(ngan_xep)
    print('---- day vao ----')
    for i in range(5):
        print("* Day vao stack bien {}".format(i))
        ngan_xep.day_vao(i)
        print(ngan_xep)

    print('----- lay ra -----')
    while not ngan_xep.rong():
        gt = ngan_xep.lay_ra()
        print('* Lay ra {}'.format(gt))
        print(ngan_xep)
        
