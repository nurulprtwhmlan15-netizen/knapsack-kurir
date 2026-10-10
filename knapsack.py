# knapsack.py
# Tiga algoritma 0/1 Knapsack untuk studi kasus kurir motor.
# Inti algoritma ditulis tanpa pustaka (hanya fungsi bawaan max dan sorted).


def knapsack_dp(paket, W):
    """Algoritma 1: mengisi tabel DP K berukuran (n+1) x (W+1)."""
    n = len(paket)
    K = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        nama, berat, ongkos = paket[i - 1]
        for w in range(W + 1):
            if berat > w:
                K[i][w] = K[i - 1][w]
            else:
                K[i][w] = max(K[i - 1][w], ongkos + K[i - 1][w - berat])
    return K


def cari_paket_terpilih(paket, K, W):
    """Algoritma 2: menelusuri tabel K untuk menemukan paket yang dibawa."""
    terpilih = []
    w = W
    for i in range(len(paket), 0, -1):
        nama, berat, ongkos = paket[i - 1]
        if K[i][w] != K[i - 1][w]:
            terpilih.append(nama)
            w = w - berat
    return terpilih


def knapsack_greedy(paket, W):
    """Pembanding: memilih paket dengan ongkos per kg tertinggi lebih dulu."""
    urut = sorted(paket, key=lambda p: p[2] / p[1], reverse=True)
    terpilih = []
    total_berat = 0
    total_ongkos = 0
    for nama, berat, ongkos in urut:
        if total_berat + berat <= W:
            terpilih.append(nama)
            total_berat = total_berat + berat
            total_ongkos = total_ongkos + ongkos
    return total_ongkos, terpilih


def knapsack_brute(paket, W, i=0):
    """Pembanding: mencoba semua kombinasi secara rekursif (bawa / tinggal)."""
    if i == len(paket):
        return 0
    nama, berat, ongkos = paket[i]
    tinggal = knapsack_brute(paket, W, i + 1)
    if berat <= W:
        bawa = ongkos + knapsack_brute(paket, W - berat, i + 1)
    else:
        bawa = 0
    return max(tinggal, bawa)


if __name__ == "__main__":
    # Kasus uji kecil (Tabel VI): (paket, W, jawaban benar)
    kasus = [
        ([("A", 1, 15), ("B", 2, 25), ("C", 3, 40), ("D", 4, 45)], 5, 65),
        ([("A", 6, 50), ("B", 2, 20), ("C", 3, 30)], 5, 50),
        ([("A", 1, 10), ("B", 2, 15), ("C", 2, 18)], 5, 43),
        ([("A", 6, 40), ("B", 7, 55)], 5, 0),
    ]
    for no, (paket, W, benar) in enumerate(kasus, start=1):
        K = knapsack_dp(paket, W)
        hasil = K[len(paket)][W]
        print("Kasus", no, "| DP:", hasil, cari_paket_terpilih(paket, K, W),
              "| Brute:", knapsack_brute(paket, W),
              "| Greedy:", knapsack_greedy(paket, W)[0],
              "| Benar:", benar, "->", "LULUS" if hasil == benar else "GAGAL")
