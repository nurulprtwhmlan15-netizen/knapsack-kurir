# eksperimen.py
# Mengukur waktu eksekusi DP, greedy, dan brute force (Tabel VII).
# Modul time hanya dipakai untuk mengukur waktu.

import time
from buat_data_paket import buat_data, simpan_csv
from knapsack import knapsack_dp, knapsack_greedy, knapsack_brute


def ukur_waktu(fungsi, paket, W, ulang=5):
    hasil_waktu = []
    for _ in range(ulang):
        mulai = time.perf_counter()
        fungsi(paket, W)
        selesai = time.perf_counter()
        hasil_waktu.append(selesai - mulai)
    rata = sum(hasil_waktu) / ulang
    simpangan = (sum((t - rata) ** 2 for t in hasil_waktu) / (ulang - 1)) ** 0.5
    return rata, simpangan


if __name__ == "__main__":
    W = 10
    for n in [5, 10, 15, 20, 25]:
        data = buat_data(n, seed=42)
        simpan_csv(data, "data/paket_n" + str(n) + ".csv")
        K = knapsack_dp(data, W)
        print(n, "DP", ukur_waktu(knapsack_dp, data, W), "ongkos", K[n][W])
        print(n, "Greedy", ukur_waktu(knapsack_greedy, data, W),
              "ongkos", knapsack_greedy(data, W)[0])
        print(n, "Brute", ukur_waktu(knapsack_brute, data, W))
