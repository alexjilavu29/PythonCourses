import pandas as pd
import matplotlib.pyplot as plt

'''Sa se incarce cele doua fisiere cars1/cars2 in dataframes.
Se observa ca fiecare df are anumite coloane empty. sa se elimine acestea. '''

cars1 = pd.read_csv("cars1_processed.csv")
cars2 = pd.read_csv("cars2_processed.csv")

# Pentru citire din fisier csv avem .read_csv

'''Numarul de observatii pentru fiecare df '''

print(len(cars1))

'''Pentru cars1 sa se afiseze primele 7 coloane '''

# Daca e nevoie de linii/coloane in functie de pozitionare se foloseste .iloc[]

print(cars1.iloc[:,:7])

'''Folosind iloc sa se afiseze toate coloanele, mai putin ultimele 3 '''

print(cars1.iloc[:,:-3])

'''Sa se construiasca un singur df pornind de la cele doua seturi de date'''

# concat este functie din pandas, deci o folosim ca si metoda la pd

print(pd.concat([cars1,cars2],axis=0))

# axis = 0 reprezinta faptul ca se concateneaza coloanele


'''Sa se citeasca setul de date fotbal.csv intr-un dataframe'''

fb = pd.read_csv("fotbal.csv")

'''Sa se afiseze echipele care au avut mai mult de 5 goluri '''

print(fb.loc[fb["Goals"]>5])

# Folosim metoda .loc daca avem conditii care utilizeaza valoarea in sine dintr-o celula anume

'''Sa se afiseze echipele care incep cu litera  R'''

print(fb[fb["Team"].str.startswith("R")])

# Putem extrage elemente cu anumite caracteristici folosind paranteze patrate cu o conditie anume

# exista .str.startswith() pentru a manipula un string

'''Sa se afiseze valorile pentru Shooting Accuracy pentru Russia, Germany si Greece'''

print(fb.loc[fb["Team"].isin(["Russia","Germany","Greece"]),["Team","Shooting Accuracy"]])

# Metoda .loc poate lua ca parametri o conditie si un set de coloane care sa fie afisate

'''Sa se afiseze randurile //(de la al treilea la al saptelea)  de la 3 la 7 si coloanele de la 3 la 6'''



'''Sa se afiseze toate randurile pana la randul numarul 4 si toate coloanele'''



'''Sa se stearga coloana -Players used-'''



'''Sa se stearga primele doua randuri '''



'''Sa se citeasca setul de date drinks intr-un dataframe '''



'''Pe ce continent se consuma, in medie, mai multa bere? '''



'''afisati statisticile pentru consumul de vin '''



'''Afisati media, mediana, minimul si maximul pentru consumul de bere pt fiecare continent'''



'''Sa se afiseze o histograma a continentelor care consuma cea mai multa bere  '''



'''Sa se citeasca setul de date tips intr-un dataframe '''



'''Au fost mai multi clienti de gen masculin sau feminin?'''



'''pentru fiecare gen, sa se calculeze valoarea minima, valoarea maxima si media tip-ului acordat'''



'''pentru fiecare tip de masa (Dinner/Lunch) sa se calculeze procentul de clienti - barbati/femei'''



'''Sa se afiseze grafic top 5 cele mai mari note de plata '''



'''folosind while sa se calculeze media a 5 numere primite de la tastatura '''

