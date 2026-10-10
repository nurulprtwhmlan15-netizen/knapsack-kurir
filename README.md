# Analisis 0/1 Knapsack dengan Dynamic Programming — Studi Kasus Kurir Motor

Kode dan data untuk laporan tugas Analisis Algoritma Komputasi
(Nurul Pratiwi, NIM D082261034, Universitas Hasanuddin).

## Isi repositori

| Berkas | Isi |
| --- | --- |
| `knapsack.py` | DP (Algoritma 1 dan 2), greedy, brute force, dan kasus uji kecil |
| `buat_data_paket.py` | Pembangkit data paket acak dengan seed tetap |
| `eksperimen.py` | Pengukuran waktu 5 kali pengulangan untuk n = 5, 10, 15, 20, 25 (W = 10 kg) |
| `grafik_eksperimen.py` | Pembuat grafik waktu eksekusi (Gambar 1) |
| `data/` | Lima dataset eksperimen (seed 42) dalam format CSV |

## Kebutuhan

- Python 3.10
- Inti algoritma tanpa pustaka. Di luar inti dipakai `random` (data), `time` (pengukuran), dan `matplotlib` (grafik; pasang dengan `pip install matplotlib`).

## Cara menjalankan

```
python knapsack.py            # menjalankan kasus uji kecil
python eksperimen.py          # mengukur waktu dan menyimpan data ke folder data/
python grafik_eksperimen.py   # membuat grafik_waktu.png
```

## Contoh keluaran `knapsack.py`

```
Kasus 1 | DP: 65 ['C', 'B'] | Brute: 65 | Greedy: 55 | Benar: 65 -> LULUS
```

Waktu eksekusi bergantung pada komputer. Hasil pada laporan diukur dengan
AMD Ryzen 5 PRO 3500U, RAM 8 GB, Windows 10 Pro 64-bit, Python 3.10.
