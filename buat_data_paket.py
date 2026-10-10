# buat_data_paket.py
# Pembuat data paket untuk eksperimen 0/1 Knapsack (studi kasus kurir motor).
# Hanya memakai modul bawaan Python (random) untuk membuat data acak,
# bukan untuk inti algoritma.

import random


def buat_data(n, seed):
    """Membuat n paket acak.
    Setiap paket: (nama, berat dalam kg, ongkos dalam ribu rupiah).
    seed tetap -> data yang sama setiap kali dijalankan (bisa diulang).
    """
    random.seed(seed)
    paket = []
    for i in range(1, n + 1):
        berat = random.randint(1, 5)      # 1 sampai 5 kg
        ongkos = random.randint(8, 30)    # Rp8.000 sampai Rp30.000
        paket.append(("P" + str(i), berat, ongkos))
    return paket


def simpan_csv(paket, nama_file):
    """Menyimpan data paket ke file CSV agar bisa dicantumkan di lampiran."""
    with open(nama_file, "w") as f:
        f.write("nama,berat_kg,ongkos_ribu\n")
        for nama, berat, ongkos in paket:
            f.write(nama + "," + str(berat) + "," + str(ongkos) + "\n")


if __name__ == "__main__":
    # Contoh: 10 paket dengan seed 42.
    # Ganti n dan seed sesuai rancangan eksperimenmu.
    data = buat_data(10, seed=42)
    for p in data:
        print(p)
    simpan_csv(data, "paket_n10.csv")
