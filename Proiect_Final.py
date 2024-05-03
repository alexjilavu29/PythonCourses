# Programare Python combinate sau individuale, minim 6 dintre următoarele facilităţi:
# - utilizarea listelor şi a dicţionarelor, incluzând metode specifice acestora; --
# - utilizarea seturilor şi a tuplurilor, incluzând metode specifice acestora; --
# - definirea şi apelarea unor funcţii; --
# - utilizarea structurilor condiţionale; --
# - utilizarea structurilor repetitive; --
# - importul unei fişier csv sau json în pachetul pandas; --
# - accesarea datelor cu loc şi iloc;
# - modificarea datelor în pachetul pandas; --
# - utilizarea funcţiilor de grup;
# - tratarea valorilor lipsă;
# - ştergerea de coloane şi înregistrări; --
# - prelucrări statistice, gruparea şi agregarea datalor în pachetul pandas;
# - prelucrarea seturilor de date cu merge / join;
# - reprezentare grafică a datelor cu pachetul matplotlib;
# - utilizarea pachetului scikit-learn (clusterizare, regresie logistică);
# - utilizarea pachetului statmodels (regresie multiplă).

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Citirea fisierului „angajati.csv”
angajati = pd.read_csv("angajati.csv")
print(angajati.head().to_string())

# Adaugarea tuturor angajatilor din sectorul „Functii de conducere” in lista „conducere”
conducere = angajati[angajati["Nume_Sector"] == "Funcții de conducere"]
print(conducere)

# Eliminarea din lista a tuturor angajatilor cu o vechime mai mica de 10 ani
conducere = conducere[conducere["Vechime"] >= 10]

# Preluarea tuturor id-urilor ca si chei si numelor angajatilor din conducere ca si valori intr-un dictionary
dict_conducere = conducere.set_index("ID_angajat").to_dict()["Nume_prenume"]
print(dict_conducere)

# Citirea fisierului „functii_angajati.csv”
functii_angajati = pd.read_csv("functii_angajati.csv")

# Asocierea id-urilor functiilor cu numele lor folosind un dictionar
dict_functii = functii_angajati.set_index("ID_funcție").to_dict()["Funcția"]

# Crearea unei liste de tupluri unde fiecare angajat din conducere este asociat cu numele functiei sale
# Mai intai, vom crea o lista de tupluri unde fiecare angajat din conducere este asociat cu id-ul functiei sale
# Apoi, vom folosi dictionarul dict_functii pentru a inlocui id-urile cu numele functiilor
angajati_functii = list(zip(conducere["ID_angajat"], conducere["ID_funcție"]))
angajati_functii = [(dict_conducere[angajat], dict_functii[functie]) for angajat, functie in angajati_functii]
print(angajati_functii)

# Determinarea sectoarelor diferite de activitate din dataframe-ul angajati folosind un set
sectoare = set(angajati["Nume_Sector"])
print(sectoare)

# Cate sectoare diferite de activitate se gasesc la CFR?
print(f"Numarul de sectoare diferite de activitate la CFR Romania este {len(sectoare)}.")

# Determinarea numarului de angajati din fiecare sector de activitate
numar_per_sector = angajati["Nume_Sector"].value_counts()
print(numar_per_sector)


# Definirea unei functii pentru calcularea salariului mediu pentru fiecare functie, data fiind o intrare din tabela functti_angajati
def salariu_mediu(row):
    return (row["Salariu_min"] + row["Salariu_max"]) / 2

# Aplicarea functiei definite anterior pe fiecare rand din tabela functii_angajati si adaugarea rezultatului in coloana „Salariu_mediu”
functii_angajati["Salariu_mediu"] = functii_angajati.apply(salariu_mediu, axis=1)
print(functii_angajati.head().to_string())

# Definirea unei functii pentru rasplatirea angajatilor cu o anumita vechime
def rasplata_vechime(row):
    procent_salariu = 0
    if row["Vechime"] == 3:
        procent_salariu += 0.05
    elif row["Vechime"] == 5:
        procent_salariu += 0.1
    elif row["Vechime"] > 5:
        i = (row["Vechime"] - (row["Vechime"] % 5)) / 5
        while i:
            procent_salariu += 0.05
            i -= 1
    return procent_salariu

# Aplicarea functiei definite anterior pe fiecare rand din tabela angajati si adaugarea rezultatului in coloana „Rasplata_vechime”
angajati["Rasplata_vechime"] = angajati.apply(rasplata_vechime, axis=1)
print(angajati.head().to_string())

# Adaugarea salariului mediu pentru fiecare angajat in tabela angajati in functie de coloana "Nume_Funcție" si salariul mediu din tabela functii_angajati
angajati["Salariu_mediu"] = angajati["Nume_Funcție"].map(functii_angajati.set_index("Funcția")["Salariu_mediu"])
print(angajati.head().to_string())

# Calcularea salariului dupa aplicarea rasplatii pentru vechime
angajati["Salariu_final"] = angajati["Salariu_mediu"] + angajati["Salariu_mediu"] * angajati["Rasplata_vechime"]
print(angajati.head().to_string())

# Stergerea coloanei „Rasplata_vechime” din tabela angajati
angajati.drop(columns="Rasplata_vechime", inplace=True)
print(angajati.head().to_string())

# Generarea statisticilor descriptive pentru salariul final
print(angajati["Salariu_final"].describe())