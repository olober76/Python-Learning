import numpy as np
from sklearn.datasets import make_blobs

def fuzzy_c_means(X, c, m, error=0.001, max_iter=100):
    n = X.shape[0] # Jumlah data
    p = X.shape[1] # Jumlah fitur
    U = np.random.rand(n, c) # Inisialisasi matriks keanggotaan U
    U = U / np.sum(U, axis=1)[:, None] # Normalisasi matriks keanggotaan U
    centroids = np.zeros((c, p)) # Inisialisasi pusat cluster
    for i in range(max_iter):
        # Hitung pusat cluster
        for j in range(c):
            centroids[j, :] = np.sum((U[:, j]**m)[:, None] * X, axis=0) / np.sum(U[:, j]**m)
        # Hitung matriks keanggotaan U
        U_new = np.zeros((n, c))
        for j in range(c):
            for k in range(n):
                num = np.linalg.norm(X[k, :] - centroids[j, :])
                den = np.sum([np.linalg.norm(X[k, :] - centroids[l, :]) for l in range(c)])
                U_new[k, j] = 1 / (1 + (num / den)**(2 / (m - 1)))
        # Hitung selisih antara matriks keanggotaan lama dan baru
        diff = np.linalg.norm(U_new - U)
        # Jika selisih sudah kurang dari error, berhenti iterasi
        if diff < error:
            break
        # Update matriks keanggotaan U
        U = U_new
    # Kembalikan pusat cluster dan matriks keanggotaan U
    return centroids, U

# Contoh penggunaan algoritma fuzzy c-means dengan data sintetis
X, y = make_blobs(n_samples=1000, centers=3, n_features=2, random_state=42)
centroids, U = fuzzy_c_means(X, c=3, m=2)

# Cetak hasil
print("Pusat cluster:")
print(centroids)
print("Matriks keanggotaan:")
print(U)
