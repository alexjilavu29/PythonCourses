# Programare Python combinate sau individuale, minim 6 dintre următoarele facilităţi:
# - utilizarea listelor şi a dicţionarelor, incluzând metode specifice acestora; --
# - utilizarea seturilor şi a tuplurilor, incluzând metode specifice acestora; --
# - definirea şi apelarea unor funcţii; --
# - utilizarea structurilor condiţionale; --
# - utilizarea structurilor repetitive; --
# - importul unei fişier csv sau json în pachetul pandas; --
# - accesarea datelor cu loc şi iloc; --
# - modificarea datelor în pachetul pandas; --
# - utilizarea funcţiilor de grup; --
# - tratarea valorilor lipsă; --
# - ştergerea de coloane şi înregistrări; --
# - prelucrări statistice, gruparea şi agregarea datalor în pachetul pandas; --
# - prelucrarea seturilor de date cu merge / join; --
# - reprezentare grafică a datelor cu pachetul matplotlib; --
# - utilizarea pachetului scikit-learn (clusterizare, regresie logistică);
# - utilizarea pachetului statmodels (regresie multiplă).

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Citirea fisierului „angajati.csv”
angajati = pd.read_csv("angajati.csv")
print(angajati.head().to_string())
print("\n")

# Eliminarea tuturor inregistrarilor care au valori lipsa in coloana „Nume_prenume”
angajati = angajati.dropna(subset=["Nume_prenume"])

# Adaugarea tuturor angajatilor din sectorul „Functii de conducere” in lista „conducere”
conducere = angajati[angajati["Nume_Sector"] == "Funcții de conducere"]
print(conducere)
print("\n")

# Eliminarea din lista a tuturor angajatilor cu o vechime mai mica de 10 ani
conducere = conducere[conducere["Vechime"] >= 10]

# Preluarea tuturor id-urilor ca si chei si numelor angajatilor din conducere ca si valori intr-un dictionary
dict_conducere = conducere.set_index("ID_angajat").to_dict()["Nume_prenume"]
print(dict_conducere)
print("\n")

# Citirea fisierului „functii_angajati.csv”
functii_angajati = pd.read_csv("functii_angajati.csv")
print(functii_angajati.head().to_string())
print("\n")


# Asocierea id-urilor functiilor cu numele lor folosind un dictionar
dict_functii = functii_angajati.set_index("ID_funcție").to_dict()["Funcția"]
print(dict_functii)
print("\n")

# Crearea unei liste de tupluri unde fiecare angajat din conducere este asociat cu numele functiei sale
angajati_functii = list(zip(conducere["ID_angajat"], conducere["ID_funcție"]))
angajati_functii = [(dict_conducere[angajat], dict_functii[functie]) for angajat, functie in angajati_functii]
print(angajati_functii)
print("\n")

# Determinarea sectoarelor diferite de activitate din dataframe-ul angajati
sectoare = set(angajati["Nume_Sector"])
print(sectoare)
print("\n")

# Determinarea numarului de sectoare diferite de activitate care se gasesc la CFR
print(f"Numarul de sectoare diferite de activitate la CFR Romania este {len(sectoare)}.")
print("\n")

# Determinarea numarului de angajati din fiecare sector de activitate
numar_per_sector = angajati["Nume_Sector"].value_counts()
print(numar_per_sector)
print("\n")


# Definirea unei functii pentru calcularea salariului mediu pentru fiecare functie,
# data fiind o intrare din tabela functii_angajati
def salariu_mediu(intrare):
    return (intrare["Salariu_min"] + intrare["Salariu_max"]) / 2

# Aplicarea functiei definite anterior pe fiecare rand din tabela functii_angajati
# si adaugarea rezultatului in coloana „Salariu_mediu”
functii_angajati["Salariu_mediu"] = functii_angajati.apply(salariu_mediu, axis=1)
print(functii_angajati.head().to_string())
print("\n")

# Definirea unei functii pentru rasplatirea angajatilor cu o anumita vechime
def rasplata_vechime(row):
    procent_salariu = 0
    if row["Vechime"] >= 10:
        i = ((row["Vechime"] - (row["Vechime"] % 5)) / 5) - 1
        procent_salariu += 0.15
        while i:
            procent_salariu += 0.05
            i -= 1
    elif row["Vechime"] >= 5:
        procent_salariu += 0.15
    elif row["Vechime"] >= 3:
        procent_salariu += 0.05
    return procent_salariu

# Aplicarea functiei definite anterior pe fiecare rand din tabela angajati si
# adaugarea rezultatului in coloana „Rasplata_vechime”
angajati["Rasplata_vechime"] = angajati.apply(rasplata_vechime, axis=1)
print(angajati.head().to_string())
print("\n")

# Adaugarea salariului mediu pentru fiecare angajat in tabela angajati in
# functie de coloana "Nume_Funcție" si salariul mediu din tabela functii_angajati
angajati["Salariu_mediu"] = angajati["Nume_Funcție"].map(functii_angajati.set_index("Funcția")["Salariu_mediu"])
print(angajati.head().to_string())
print("\n")

# Calcularea salariului dupa aplicarea rasplatii pentru vechime
angajati["Salariu_final"] = angajati["Salariu_mediu"] + angajati["Salariu_mediu"] * angajati["Rasplata_vechime"]
print(angajati.head().to_string())
print("\n")

# Stergerea coloanei „Rasplata_vechime” din tabela angajati
angajati.drop(columns="Rasplata_vechime", inplace=True)
print(angajati.head().to_string())
print("\n")

# Generarea statisticilor descriptive pentru salariul final
print(angajati["Salariu_final"].describe())
print("\n")


# Crearea unui grafic care sa arate distributia salariilor finale
plt.figure(figsize=(10, 6))
sns.histplot(angajati["Salariu_final"], bins=30, color='skyblue')
plt.title('Distributia Salariilor Finale')
plt.xlabel('Salariu Final')
plt.ylabel('Numar de Angajati')
plt.show()

# Crearea unui grafic care sa arate distributia salariilor finale folosind matplotlib
plt.figure(figsize=(10, 6))
plt.hist(angajati["Salariu_final"], bins=30, color='blue')
plt.title('Distributia Salariilor Finale')
plt.xlabel('Salariu Final')
plt.ylabel('Numar de Angajati')
plt.show()

# Localizarea angajatilor cu prenumele "Maria" care au salariul final mai mare de 10000
# Prenumele se va obtine prin determinarea celui de-al doilea cuvant din variabila "Nume_prenume"
angajati["Prenume"] = angajati["Nume_prenume"].apply(lambda x: x.split()[1])
angajati_maria = angajati.loc[(angajati["Prenume"] == "Maria")
                              & (angajati["Salariu_final"] > 10000),
["Nume_prenume", "Nume_Funcție", "Salariu_final"]]
print(angajati_maria.to_string())
print("\n")

# Preluarea înregistrărilor din tabela angajati_maria de pe pozitiile 1 si 3
print(angajati_maria.iloc[[0, 2]])


# Gruparea funcțiilor după intervalele de salariere din variabila "Clasificare Salariu Maxim"
# si calcularea salariului mediu si mediana pentru fiecare grup
statistici_salarii_per_interval = (functii_angajati.groupby("Clasificare Salariu Maxim")["Salariu_mediu"]
                                   .agg(["mean", "median"]))
print(statistici_salarii_per_interval)
print("\n")

# Vom folosi tabelele angajati si functii_angajati pentru a realiza un inner join pe coloana „ID_funcție”
# Vom folosi functia merge pentru a realiza operatia de join
# Vom folosi parametrul „on” pentru a specifica coloana dupa care se va realiza join-ul
# Rezultatul va fi stocat in variabila „angajati_functii”
angajati_functii = pd.merge(angajati, functii_angajati, on="ID_funcție")
# Vom afisa doar coloanele "Num_prenume", "Nume_Funcție" si "Nume_Sector"
print(angajati_functii[["Nume_prenume", "Funcția", "Nume_Sector"]].to_string())
