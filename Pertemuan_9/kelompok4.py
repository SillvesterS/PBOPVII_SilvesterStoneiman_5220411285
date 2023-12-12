# Kelas induk
class Animal:
    def __init__(self, nama, sifat, ukuran, jmlh_kaki):
        self.nama = nama
        self.sifat = sifat
        self.ukuran = ukuran
        self.jmlh_kaki = jmlh_kaki

# Turunan dari kelas Animal: Mamalia
class Mamalia(Animal):
    def __init__(self, nama, sifat, ukuran, jmlh_kaki, bisa_jalan, jenis_mamalia):
        super().__init__(nama, sifat, ukuran, jmlh_kaki)
        self.bisa_jalan = bisa_jalan
        self.jenis_mamalia = jenis_mamalia

    def describe(self):
        return f"{self.nama} adalah hewan {self.sifat} dengan ukuran {self.ukuran} dan memiliki {self.jmlh_kaki} kaki. Jenisnya adalah {self.jenis_mamalia} dan {'bisa' if self.bisa_jalan else 'tidak bisa'} berjalan."

# Turunan dari kelas Animal: Aves
class Aves(Animal):
    def __init__(self, nama, sifat, ukuran, jmlh_kaki, bisa_terbang, jenis_aves):
        super().__init__(nama, sifat, ukuran, jmlh_kaki)
        self.bisa_terbang = bisa_terbang
        self.jenis_aves = jenis_aves

    def describe(self):
        return f"{self.nama} adalah hewan {self.sifat} dengan ukuran {self.ukuran} dan memiliki {self.jmlh_kaki} kaki. Jenisnya adalah {self.jenis_aves} dan {'bisa' if self.bisa_terbang else 'tidak bisa'} terbang."

# Turunan dari kelas Aves: Ayam
class Ayam(Aves):
    def __init__(self, nama, sifat, ukuran, jmlh_kaki, bisa_terbang, jenis_aves, jenis_ayam, bisa_diadu):
        super().__init__(nama, sifat, ukuran, jmlh_kaki, bisa_terbang, jenis_aves)
        self.jenis_ayam = jenis_ayam
        self.bisa_diadu = bisa_diadu

    def describe(self):
        return f"{self.nama} adalah hewan {self.sifat} dengan ukuran {self.ukuran} dan memiliki {self.jmlh_kaki} kaki. Jenisnya adalah {self.jenis_ayam} dan {'bisa' if self.bisa_diadu else 'tidak bisa'} diadu."
    
# Turunan dari kelas Aves: Merpati
class Merpati(Aves):
    def __init__(self, nama, sifat, ukuran, jmlh_kaki, bisa_terbang, jenis_aves):
        super().__init__(nama, sifat, ukuran, jmlh_kaki, bisa_terbang, jenis_aves)

    def describe(self):
        return f"{self.nama} adalah hewan {self.sifat} dengan ukuran {self.ukuran} dan memiliki {self.jmlh_kaki} kaki. Jenisnya adalah {self.jenis_aves} dan {'bisa' if self.bisa_terbang else 'tidak bisa'} terbang tinggi."

# Membuat objek-objek dari kelas-kelas yang telah didefinisikan
singa = Mamalia("Singa", "predator", "besar", 4, True, "Singa Putih")
kuda = Mamalia("Kuda", "herbivora", "sedang", 4, True, "Kuda Perang")
gajah = Mamalia("Gajah", "herbivora", "besar", 4, True, "Gajah Asia")
ayam = Ayam("Ayam", "omnivora", "sedang", 2, True,"Ayam","Ayam Cemani", False)
merpati = Merpati("Merpati", "omnivora", "sedang", 2, True, "Merpati Flight")

# Mencetak deskripsi masing-masing hewan
print()
print('---MAMALIA---')
print(singa.describe())
print(kuda.describe())
print(gajah.describe())
print()
print('---AVES---')
print(ayam.describe())
print(merpati.describe())
print()

