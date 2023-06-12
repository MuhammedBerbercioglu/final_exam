import pandas as pd
import numpy as np

columns = ["age", "income", "student", "credit_rating", "computer"]
data = np.array(
    [
        ["genc", "high", False, "fair", False],
        ["genc", "high", False, "excellent", False],
        ["orta_yasli", "high", False, "fair", True],
        ["yasli", "medium", False, "fair", True],
        ["yasli", "low", True, "fair", True],
        ["yasli", "low", True, "excellent", False],
        ["orta_yasli", "low", True, "excellent", True],
        ["genc", "medium", False, "fair", False],
        ["genc", "low", True, "fair", True],
        ["yasli", "medium", True, "fair", True],
        ["genc", "medium", True, "excellent", True],
        ["orta_yasli", "medium", False, "excellent", True],
        ["orta_yasli", "high", True, "fair", True],
        ["yasli", "medium", False, "excellent", False],
    ]
)


# Dataframe oluştur
dataframe = pd.DataFrame(data, columns=columns)
dataframe["student"] = dataframe["student"].map({"True": True, "False": False})
dataframe["computer"] = dataframe["computer"].map({"True": True, "False": False})

total_count = len(dataframe)

# P(Ci) hesap ve yazdır
C_buys_comp_yes = len(dataframe[dataframe["computer"] == True])
C_buys_comp_no = len(dataframe[dataframe["computer"] == False])

P0y = C_buys_comp_yes / total_count
P0n = C_buys_comp_no / total_count

print("P(Ci):")
print(f"\tP(buys_computer = 'yes') = {C_buys_comp_yes}/{total_count} = {P0y:.3f}")
print(f"\tP(buys_computer = 'no') = {C_buys_comp_no}/{total_count} = {P0n:.3f}")

#  P(X|Ci) hesap ve yazdır
C_genc_bc_yes = len(
    dataframe[(dataframe["computer"] == True) & (dataframe["age"] == "genc")]
)
C_genc_bc_no = len(
    dataframe[(dataframe["computer"] == False) & (dataframe["age"] == "genc")]
)
P1y = C_genc_bc_yes / C_buys_comp_yes
P1n = C_genc_bc_no / C_buys_comp_no

C_medium_bc_yes = len(
    dataframe[(dataframe["computer"] == True) & (dataframe["income"] == "medium")]
)
C_medium_bc_no = len(
    dataframe[(dataframe["computer"] == False) & (dataframe["income"] == "medium")]
)
P2y = C_medium_bc_yes / C_buys_comp_yes
P2n = C_medium_bc_no / C_buys_comp_no

C_student_bc_yes = len(
    dataframe[(dataframe["computer"] == True) & (dataframe["student"] == True)]
)
C_student_bc_no = len(
    dataframe[(dataframe["computer"] == False) & (dataframe["student"] == True)]
)
P3y = C_student_bc_yes / C_buys_comp_yes
P3n = C_student_bc_no / C_buys_comp_no

C_fair_bc_yes = len(
    dataframe[(dataframe["computer"] == True) & (dataframe["credit_rating"] == "fair")]
)
C_fair_bc_no = len(
    dataframe[(dataframe["computer"] == False) & (dataframe["credit_rating"] == "fair")]
)
P4y = C_fair_bc_yes / C_buys_comp_yes
P4n = C_fair_bc_no / C_buys_comp_no

print("\nHer sınıf için P(X|Ci) hesapla:")

print(f"\tP(age = 'genc' | buys_computer = 'yes') = {C_genc_bc_yes}/{C_buys_comp_yes} = {P1y:.3f}")
print(f"\tP(age = 'genc' | buys_computer = 'no') = {C_genc_bc_no}/{C_buys_comp_no} = {P1n:.3f}")

print(f"\tP(income = 'medium' | buys_computer = 'yes') = {C_medium_bc_yes}/{C_buys_comp_yes} = {P2y:.3f}")
print(f"\tP(income = 'medium' | buys_computer = 'no') = {C_medium_bc_no}/{C_buys_comp_no} = {P2n:.3f}")

print(f"\tP(student = 'yes' | buys_computer = 'yes') = {C_student_bc_yes}/{C_buys_comp_yes} = {P3y:.3f}")
print(f"\tP(student = 'yes' | buys_computer = 'no') = {C_student_bc_no}/{C_buys_comp_no} = {P3n:.3f}")

print(f"\tP(credit_rating = 'fair' | buys_computer = 'yes') = {C_fair_bc_yes}/{C_buys_comp_yes} = {P4y:.3f}")
print(f"\tP(credit_rating = 'fair' | buys_computer = 'no') = {C_fair_bc_no}/{C_buys_comp_no} = {P4n:.3f}")

print("\nX = (age = genc, income = medium, student = yes, credit_rating = fair)")
print("\nP(X|Ci):")

PX_yes = P1y * P2y * P3y * P4y
PX_no = P1n * P2n * P3n * P4n

print(f"\tP(X | buys_computer = 'yes') = {P1y:.3f}*{P2y:.3f}*{P3y:.3f}*{P4y:.3f} = {PX_yes:.3f}")
print(f"\tP(X | buys_computer = 'no') = {P1n:.3f}*{P2n:.3f}*{P3n:.3f}*{P4n:.3f} = {PX_no:.3f}")

print("\nP(X|Ci) * P(Ci):")
P_YES = PX_yes * P0y
P_NO = PX_no * P0n

print(f"\tP(X | buys_computer = 'yes') * P(buys_computer = 'yes') = {PX_yes:.3f} * {P0y:.3f} = {P_YES:.3f}")
print(f"\tP(X | buys_computer = 'no') * P(buys_computer = 'no') = {PX_no:.3f} * {P0n:.3f} = {P_NO:.3f}")


if(P_YES > P_NO):
    print("\n\n X örneği 'buys_computer = yes' sınıfına aittir.")
else:
    print("\n\n X örneği 'buys_computer = no' sınıfına aittir.")
