class BangBam:
    def __init__(self, kich_thuoc = 10):
        self.danh_sach = [None for _ in range(kich_thuoc)]
        

    def __str__(self):
        kq = '['
        stt1 = 0
        for x in self.danh_sach:
            stt1 = stt1 + 1
            if stt1 != 1:
                kq = kq + ', '
            if x is None:
                kq = kq + '[None]'
            else:
                kq = kq + '['
                stt2 = 0
                for e in x:
                    stt2 += 1
                    if stt2 != 1:
                        kq = kq + ', '
                    kq = kq + str(e[0]) + ': ' + str(e[1])
                kq = kq + ']'

        kq = kq + ']'
        return kq



    def bam(self, khoa):
        kich_thuoc = len(self.danh_sach)
        return hash(khoa)%kich_thuoc



    def them(self, khoa, gia_tri):
        chi_muc = self.bam(khoa)
        if self.danh_sach[chi_muc] is None:
            self.danh_sach[chi_muc] = list()
            self.danh_sach[chi_muc].append([khoa, gia_tri])
        else:
            cap_nhap = False
            for x in self.danh_sach[chi_muc]:
                if x[0] == khoa:
                    x[1] = gia_tri
                    cap_nhap = True
                    break

            if cap_nhap == False:
                self.danh_sach[chi_muc].append([khoa, gia_tri])
                
                    

    def lay(self, khoa):
        chi_muc = self.bam(khoa)
        if self.danh_sach[chi_muc] is None:
            return None
        else:
            for x in self.danh_sach[chi_muc]:
                if x[0] == khoa:
                    return x[1]
                
            


    def __setitem__(self, khoa, gia_tri):
        self.them(khoa, gia_tri)


    def __getitem__(self, khoa):
        return self.lay(khoa)


def main():
    bang_bam = BangBam()
    import random
    for _ in range(18):
        khoa = random.randint(0, 10)
        gia_tri = random.randint(10, 100)
        print("Them khoa = {}, gia tri = {}".format(khoa, gia_tri))
        bang_bam[khoa] = gia_tri
        print(bang_bam)
        print()

    khoa = int(input("Nhap vao mot khoa: "))
    gia_tri = bang_bam[khoa]
    print("Khoa {} co gia tri la {}".format(khoa, gia_tri))
    


if __name__ == '__main__':
    main()
