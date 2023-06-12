import pandas as pd
import numpy as np
from math import sqrt

# Görüntüleme için precision virgülden sonra iki basamak olarak ayarla
pd.options.display.precision = 2

# X ve Y veri tablosu
columns = ["X", "Y", "Z"]
data = np.array(
    [
        [1, 3, -1],
        [2, 5, 1],
        [2, 3, 1],
        [3, 9, -1],
        [4, 7, -1],
        [5, 2, 1],
        [6, 8, 1],
        [8, 6, -1],
        [10, 6, -1],
        [11, 1, -1],
    ]
)

# Dataframe oluştur
dataframe = pd.DataFrame(data, columns=columns)
dataframe["Z"] = np.where(dataframe["Z"] > 0, "Pozitif", "Negatif")
print("Veri Tablosu:")
print(dataframe)

# Yeni nokta
new_point = (7, 3)
print("\n\n")
print(f"Yeni değer: X={new_point[0]}, Y={new_point[1]}")

# İki nokta arasında öklid mesafesini hesaplayan method
def calc_euclid_distance(point1, point2):
    dx = abs(point1[0] - point2[0])
    dy = abs(point1[1] - point2[1])
    return sqrt(pow(dx, 2) + pow(dy, 2))


# Öklid mesafesini hesapla
dataframe["MESAFE"] = dataframe.apply(
    lambda x: calc_euclid_distance((x["X"], x["Y"]), new_point), axis=1
)
dataframe["SIRALAMA"] = dataframe["MESAFE"].rank(method="first")

print("\n\n")
print("Mesafe ve Sıralama hesapları:")
print(dataframe)

# En yakın 3 komşuyu filtrele
dataframe[["SIRALAMA"]] = dataframe[dataframe[["SIRALAMA"]] <= 3][["SIRALAMA"]]
dataframe2 = dataframe.dropna()

print("\n\n")
print("En yakın 3 komşu:")
print(dataframe2)

pos = len(dataframe2[dataframe2["Z"]=="Pozitif"])
neg = len(dataframe2[dataframe2["Z"]=="Negatif"])
sinif = "Pozitif" if pos > neg else "Negatif"

print("\n\n")
print(f"En yakın 3 komşudan {pos} adet Pozitif, {neg} adet Negatif sınıfında. Yeni değer ({sinif}) sınıfına ait olarak belirlendi.")

