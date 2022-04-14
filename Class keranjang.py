class keranjang():
    jumlah_keranjang = 0
    def _init_(self,input_nama,input_isi):
        self.nama=input_nama
        self.isi=input_isi
        keranjang.jumlah_keranjang +=1
#main program
keranjang1=keranjang("keranjang satu(1)","buah")
keranjang2=keranjang("kernjang dua(2)","sayur")
keranjang3=keranjang("kernjang dua(2)","sayur")

print(keranjang.jumlah_keranjang)
