import pandas as pd
import numpy as np

# Görüntüleme için precision virgülden sonra iki basamak olarak ayarla
pd.options.display.precision = 2

# Personel bilgileri
columns_1 = ["PERSONEL", "MAAŞ", "DENEYİM", "GÖREV", "MEMNUN"]
data_1 = np.array(
    [
        [1, "NORMAL", "ORTA", "UZMAN", "EVET"],
        [2, "YÜKSEK", "YOK", "UZMAN", "EVET"],
        [3, "DÜŞÜK", "YOK", "YÖNETİCİ", "EVET"],
        [4, "YÜKSEK", "ORTA", "YÖNETİCİ", "EVET"],
        [5, "DÜŞÜK", "ORTA", "YÖNETİCİ", "EVET"],
        [6, "YÜKSEK", "İYİ", "YÖNETİCİ", "EVET"],
        [7, "DÜŞÜK", "İYİ", "YÖNETİCİ", "EVET"],
        [8, "YÜKSEK", "ORTA", "UZMAN", "HAYIR"],
        [9, "DÜŞÜK", "ORTA", "UZMAN", "HAYIR"],
        [10, "YÜKSEK", "İYİ", "UZMAN", "HAYIR"],
        [11, "DÜŞÜK", "İYİ", "UZMAN", "HAYIR"],
    ]
)

# Personel bilgileri dataframe'i
dataframe = pd.DataFrame(data_1, columns=columns_1, index=data_1[:, 0])
print("Personel Bilgileri")
print(dataframe)

# Aday bölünmeler dataframe'i
columns_2 = ["BÖLÜNME", "SOL", "SAĞ", "SOL_EVET", "SAĞ_EVET"]
data_2 = np.array(
    [
        [1, 0, 0, 0, 0],
        [2, 0, 0, 0, 0],
        [3, 0, 0, 0, 0],
        [4, 0, 0, 0, 0],
        [5, 0, 0, 0, 0],
        [6, 0, 0, 0, 0],
        [7, 0, 0, 0, 0],
        [8, 0, 0, 0, 0],
    ]
)
dataframe2 = pd.DataFrame(data_2, columns=columns_2, index=data_2[:, 0])

# Aday bölünmeler verilerini çek
for x in range(1, 12):
    personel_data = dataframe.loc[str(x)]
    is_memnun = personel_data["MEMNUN"] == "EVET"

    # Maaş bölünmeler
    if personel_data["MAAŞ"] == "NORMAL":
        dataframe2.at[1, "SOL"] = dataframe2.at[1, "SOL"] + 1
        dataframe2.at[2, "SAĞ"] = dataframe2.at[2, "SAĞ"] + 1
        dataframe2.at[3, "SAĞ"] = dataframe2.at[3, "SAĞ"] + 1

        if is_memnun:
            dataframe2.at[1, "SOL_EVET"] = dataframe2.at[1, "SOL_EVET"] + 1
            dataframe2.at[2, "SAĞ_EVET"] = dataframe2.at[2, "SAĞ_EVET"] + 1
            dataframe2.at[3, "SAĞ_EVET"] = dataframe2.at[3, "SAĞ_EVET"] + 1
    elif personel_data["MAAŞ"] == "YÜKSEK":
        dataframe2.at[1, "SAĞ"] = dataframe2.at[1, "SAĞ"] + 1
        dataframe2.at[2, "SOL"] = dataframe2.at[2, "SOL"] + 1
        dataframe2.at[3, "SAĞ"] = dataframe2.at[3, "SAĞ"] + 1

        if is_memnun:
            dataframe2.at[1, "SAĞ_EVET"] = dataframe2.at[1, "SAĞ_EVET"] + 1
            dataframe2.at[2, "SOL_EVET"] = dataframe2.at[2, "SOL_EVET"] + 1
            dataframe2.at[3, "SAĞ_EVET"] = dataframe2.at[3, "SAĞ_EVET"] + 1
    elif personel_data["MAAŞ"] == "DÜŞÜK":
        dataframe2.at[1, "SAĞ"] = dataframe2.at[1, "SAĞ"] + 1
        dataframe2.at[2, "SAĞ"] = dataframe2.at[2, "SAĞ"] + 1
        dataframe2.at[3, "SOL"] = dataframe2.at[3, "SOL"] + 1

        if is_memnun:
            dataframe2.at[1, "SAĞ_EVET"] = dataframe2.at[1, "SAĞ_EVET"] + 1
            dataframe2.at[2, "SAĞ_EVET"] = dataframe2.at[2, "SAĞ_EVET"] + 1
            dataframe2.at[3, "SOL_EVET"] = dataframe2.at[3, "SOL_EVET"] + 1

    # Deneyim bölünmeler
    if personel_data["DENEYİM"] == "YOK":
        dataframe2.at[4, "SOL"] = dataframe2.at[4, "SOL"] + 1
        dataframe2.at[5, "SAĞ"] = dataframe2.at[5, "SAĞ"] + 1
        dataframe2.at[6, "SAĞ"] = dataframe2.at[6, "SAĞ"] + 1

        if is_memnun:
            dataframe2.at[4, "SOL_EVET"] = dataframe2.at[4, "SOL_EVET"] + 1
            dataframe2.at[5, "SAĞ_EVET"] = dataframe2.at[5, "SAĞ_EVET"] + 1
            dataframe2.at[6, "SAĞ_EVET"] = dataframe2.at[6, "SAĞ_EVET"] + 1
    elif personel_data["DENEYİM"] == "ORTA":
        dataframe2.at[4, "SAĞ"] = dataframe2.at[4, "SAĞ"] + 1
        dataframe2.at[5, "SOL"] = dataframe2.at[5, "SOL"] + 1
        dataframe2.at[6, "SAĞ"] = dataframe2.at[6, "SAĞ"] + 1

        if is_memnun:
            dataframe2.at[4, "SAĞ_EVET"] = dataframe2.at[4, "SAĞ_EVET"] + 1
            dataframe2.at[5, "SOL_EVET"] = dataframe2.at[5, "SOL_EVET"] + 1
            dataframe2.at[6, "SAĞ_EVET"] = dataframe2.at[6, "SAĞ_EVET"] + 1
    elif personel_data["DENEYİM"] == "İYİ":
        dataframe2.at[4, "SAĞ"] = dataframe2.at[4, "SAĞ"] + 1
        dataframe2.at[5, "SAĞ"] = dataframe2.at[5, "SAĞ"] + 1
        dataframe2.at[6, "SOL"] = dataframe2.at[6, "SOL"] + 1

        if is_memnun:
            dataframe2.at[4, "SAĞ_EVET"] = dataframe2.at[4, "SAĞ_EVET"] + 1
            dataframe2.at[5, "SAĞ_EVET"] = dataframe2.at[5, "SAĞ_EVET"] + 1
            dataframe2.at[6, "SOL_EVET"] = dataframe2.at[6, "SOL_EVET"] + 1

    # Görev bölünmeler
    if personel_data["GÖREV"] == "UZMAN":
        dataframe2.at[7, "SOL"] = dataframe2.at[7, "SOL"] + 1
        dataframe2.at[8, "SAĞ"] = dataframe2.at[8, "SAĞ"] + 1

        if is_memnun:
            dataframe2.at[7, "SOL_EVET"] = dataframe2.at[7, "SOL_EVET"] + 1
            dataframe2.at[8, "SAĞ_EVET"] = dataframe2.at[8, "SAĞ_EVET"] + 1
    elif personel_data["GÖREV"] == "YÖNETİCİ":
        dataframe2.at[7, "SAĞ"] = dataframe2.at[7, "SAĞ"] + 1
        dataframe2.at[8, "SOL"] = dataframe2.at[8, "SOL"] + 1

        if is_memnun:
            dataframe2.at[7, "SAĞ_EVET"] = dataframe2.at[7, "SAĞ_EVET"] + 1
            dataframe2.at[8, "SOL_EVET"] = dataframe2.at[8, "SOL_EVET"] + 1

print("\nAday Bölünmeler")
print(dataframe2)

# Memnun 'HAYIR' sayılarını hesapla
dataframe2["SOL_HAYIR"] = dataframe2["SOL"] - dataframe2["SOL_EVET"]
dataframe2["SAĞ_HAYIR"] = dataframe2["SAĞ"] - dataframe2["SAĞ_EVET"]

# Sol ve Sağ için İki ayrı dataframe oluştur
dataframe3 = dataframe2[["BÖLÜNME", "SOL", "SOL_EVET", "SOL_HAYIR"]].copy()
dataframe4 = dataframe2[["BÖLÜNME", "SAĞ", "SAĞ_EVET", "SAĞ_HAYIR"]].copy()

# Yüzdeleri hesapla
dataframe3["P_SOL"] = dataframe3["SOL"] / 11
dataframe3["P_SOL_EVET"] = dataframe3["SOL_EVET"] / dataframe3["SOL"]
dataframe3["P_SOL_HAYIR"] = dataframe3["SOL_HAYIR"] / dataframe3["SOL"]

dataframe4["P_SAĞ"] = dataframe4["SAĞ"] / 11
dataframe4["P_SAĞ_EVET"] = dataframe4["SAĞ_EVET"] / dataframe4["SAĞ"]
dataframe4["P_SAĞ_HAYIR"] = dataframe4["SAĞ_HAYIR"] / dataframe4["SAĞ"]

print("\nBölünmeler SOL")
print(dataframe3)

print("\nBölünmeler SAĞ")
print(dataframe4)

# Uygunluk değerlerini hesapla
dataframe5 = dataframe2[["BÖLÜNME"]].copy()
dataframe5["P_SOL"] = dataframe3["P_SOL"]
dataframe5["P_SAĞ"] = dataframe4["P_SAĞ"]
dataframe5["2PsolPsağ"] = 2 * dataframe5["P_SOL"] * dataframe5["P_SAĞ"]
dataframe5["DELTA_EVET"] = (dataframe3["P_SOL_EVET"] - dataframe4["P_SAĞ_EVET"]).abs()
dataframe5["DELTA_HAYIR"] = (dataframe3["P_SOL_HAYIR"] - dataframe4["P_SAĞ_HAYIR"]).abs()
dataframe5["UYGUNLUK"] = dataframe5["2PsolPsağ"] * (dataframe5["DELTA_EVET"] + dataframe5["DELTA_HAYIR"])

print("\n")
print(dataframe5)

print(f"\nEn yüksek uygunluk değerine sahip bölünme(ler) {dataframe5.UYGUNLUK.max():.2f} değeri ile")
print(dataframe5[dataframe5.UYGUNLUK == dataframe5.UYGUNLUK.max()][["BÖLÜNME", "UYGUNLUK"]])