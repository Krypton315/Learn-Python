class Mobil:
	def __init__(self, merk, warna):
		self.merk = merk
		self.warna = warna
		self.kecepatan = 0

	def tambah_kecepatan(self, jumlah):
		self.kecepatan += jumlah
		return self.kecepatan

class MobilListrik(Mobil):
	def __init__(self, merk, warna):
		super().__init__(merk, warna)
		self.baterai = 100

	def tambah_kecepatan(self, jumlah):
		self.baterai -= 5

	def isi_daya(self):
		self.baterai = 100
		print("Baterai mobil {self.merk} telah diisi penuh!")

mobil_leo = MobilListrik("Tesla", "Putih")

print(mobil_leo.tambah_kecepatan(60))
print(mobil_leo.baterai)