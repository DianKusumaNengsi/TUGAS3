class keranjang():
    jenis = "buah"
    __nilai = 0 #private

    def _init_(self,input_nama,input_warna):
        self.nama=input_nama
        self.warna=input_warna

    def kj1(self,input_nilai):
        self.__nilai += input_nilai

    def kj2(self,input_nilai):
        self.__nilai += input_nilai

    def jumlah_diskon(self):
        if self.__nilai <=50:
            print(self.nama,'dapat diskon 10%')
        else:
            print(self.nama,'tudak ada diskon')


mangga = keranjang("buah mangga ","hijau")
rambutan = keranjang("buah rambutan","merah")

mangga.kj1(10)
mangga.kj2(50)
mangga.jumlah_diskon()

rambutan.kj1(10)
rambutan.kj2(20)
rambutan.jumlah_diskon()

print(keranjang.__nilai)
