# grafik_eksperimen.py
# Grafik waktu eksekusi terhadap n, disandingkan dengan kurva teoretis.
# matplotlib hanya untuk menggambar grafik (diizinkan di ketentuan tugas).

import math
import matplotlib.pyplot as plt

W = 10
n = [5, 10, 15, 20, 25]
dp = [13.1, 23.7, 31.3, 42.4, 52.5]        # µs
greedy = [4.0, 4.0, 4.9, 6.9, 9.2]         # µs
brute_n = [5, 10, 15, 20, 25]
brute = [16.2, 171.8, 936.9, 4366.8, 15560.4]        # µs

# Kurva teoretis diskalakan agar melewati titik ukur terakhir.
# (Konstanta c bergantung pada komputer, jadi yang dibandingkan adalah BENTUK kurvanya.)
c_dp = dp[-1] / (n[-1] * W)
c_gr = greedy[-1] / (n[-1] * math.log2(n[-1]))
c_br = brute[-1] / (2 ** brute_n[-1])

teori_dp = [c_dp * x * W for x in n]
teori_gr = [c_gr * x * math.log2(x) for x in n]
teori_br = [c_br * 2 ** x for x in brute_n]

plt.figure(figsize=(7, 4.5))
plt.plot(n, dp, "o-", color="tab:blue", label="DP (terukur)")
plt.plot(n, teori_dp, "--", color="tab:blue", label="O(nW) teoretis")
plt.plot(n, greedy, "s-", color="tab:green", label="Greedy (terukur)")
plt.plot(n, teori_gr, "--", color="tab:green", label="O(n log n) teoretis")
plt.plot(brute_n, brute, "^-", color="tab:red", label="Brute force (terukur)")
plt.plot(brute_n, teori_br, "--", color="tab:red", label="O(2^n) teoretis")

plt.yscale("log")
plt.xlabel("Jumlah paket (n)")
plt.ylabel("Waktu eksekusi (µs, skala log)")
plt.title("Waktu eksekusi terhadap n (W = 10 kg)")
plt.grid(True, which="both", alpha=0.3)
plt.legend(fontsize=8)
plt.tight_layout()
plt.savefig("grafik_waktu.png", dpi=200)
plt.show()
