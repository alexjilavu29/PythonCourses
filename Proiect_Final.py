# Programare Python combinate sau individuale, minim 6 dintre următoarele facilităţi:
# - utilizarea listelor şi a dicţionarelor, incluzând metode specifice acestora;
# - utilizarea seturilor şi a tuplurilor, incluzând metode specifice acestora;
# - definirea şi apelarea unor funcţii;
# - utilizarea structurilor condiţionale;
# - utilizarea structurilor repetitive;
# - importul unei fişier csv sau json în pachetul pandas;
# - accesarea datelor cu loc şi iloc;
# - modificarea datelor în pachetul pandas;
# - utilizarea funcţiilor de grup;
# - tratarea valorilor lipsă;
# - ştergerea de coloane şi înregistrări;
# - prelucrări statistice, gruparea şi agregarea datalor în pachetul pandas;
# - prelucrarea seturilor de date cu merge / join;
# - reprezentare grafică a datelor cu pachetul matplotlib;
# - utilizarea pachetului scikit-learn (clusterizare, regresie logistică);
# - utilizarea pachetului statmodels (regresie multiplă).

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

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