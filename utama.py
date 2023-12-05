from cth_class import Lingkaran,PersegiPanjang,MataKuliah

Lingkaran_a = Lingkaran(3)
Lingkaran_b = Lingkaran(5)

pp_1 = PersegiPanjang(3,4)
pp_2 = PersegiPanjang(2,6)

print(Lingkaran_b.radius)
print(f"persegi panjang 1 memiliki panjang {pp_1.pjg}")
print(f"persegi panjang 2 memiliki panjang {pp_2.lbr}")

proglanj = MataKuliah("TI6383,", "pemrograman lanjut",3)
print(proglanj.kode)
print(proglanj.nama)
print(proglanj.sks)