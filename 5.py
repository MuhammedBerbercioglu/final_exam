import pandas as pd
import numpy as np
from sklearn import linear_model

columns = ["X1", "X2", "X3", "X4", "Y1", "Y2", "Y3"]
data = [
    [5.1, 3.5, 1.4, 0.2, 1, 0, 0],
    [4.9, 3, 1.4, 0.2, 1, 0, 0],
    [7, 3.2, 4.7, 1.4, 0, 1, 0],
    [6.4, 3.2, 4.5, 1.5, 0, 1, 0],
    [6.3, 3.3, 6, 2.5, 0, 0, 1],
    [5.8, 2.7, 5.1, 1.9, 0, 0, 1],
]

# Dataframe oluştur
dataframe = pd.DataFrame(data, columns=columns)

print(dataframe)

X = dataframe[["X1", "X2", "X3", "X4"]]
y = dataframe[["Y1", "Y2", "Y3"]]

regr = linear_model.LinearRegression()
regr.fit(X, y)

print("\nHesaplanan katsayılar:")
print(f"Y1 = {regr.intercept_[0]:.1f} + {regr.coef_[0][0]:.2f} X1 + {regr.coef_[0][1]:.2f} X2 + {regr.coef_[0][2]:.2f} X3 + {regr.coef_[0][3]:.2f} X4")
print(f"Y2 = {regr.intercept_[1]:.1f} + {regr.coef_[1][0]:.2f} X1 + {regr.coef_[1][1]:.2f} X2 + {regr.coef_[1][2]:.2f} X3 + {regr.coef_[1][3]:.2f} X4")
print(f"Y3 = {regr.intercept_[2]:.1f} + {regr.coef_[2][0]:.2f} X1 + {regr.coef_[2][1]:.2f} X2 + {regr.coef_[2][2]:.2f} X3 + {regr.coef_[2][3]:.2f} X4")

new_values = [5, 3.4, 1.5, 0.2]
# new_values = {"X1": 5, "X2": 3.4, "X3": 1.5, "X4": 0.2}
new_values = pd.DataFrame(data=[new_values], columns=["X1", "X2", "X3", "X4"])
print("\nYeni X değerleri:")
print(new_values)

prediction = regr.predict(new_values)
predict_y_values = np.round(prediction[0]).astype("int")

dataframe2 = pd.DataFrame().reindex_like(dataframe).dropna()
dataframe2.loc[len(dataframe2)] = np.concatenate([new_values.iloc[0], predict_y_values])
dataframe2[["Y1", "Y2", "Y3"]] = dataframe2[["Y1", "Y2", "Y3"]].astype("int")
print("\nYeni değerlerin sınıflandırma hesapları:")
print(dataframe2)

y1 = predict_y_values[0]
y2 = predict_y_values[1]
y3 = predict_y_values[2]

print(f"\nHesaplanan değerler Y1 = {y1}, Y2 = {y2}, Y3 = {y3}")
if y1 == 1:
    print("\tBu Y değerlerine göre sınıfı: 'A' olarak hesaplanmıştır.")
if y2 == 1:
    print("\tBu Y değerlerine göre sınıfı: 'B' olarak hesaplanmıştır.")
if y3 == 1:
    print("\tBu Y değerlerine göre sınıfı: 'C' olarak hesaplanmıştır.")
