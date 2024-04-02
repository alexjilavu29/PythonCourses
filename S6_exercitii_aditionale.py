import pandas as pd
import matplotlib.pyplot as plt

'''Sa se incarce cele doua fisiere cars1/cars2 in dataframes.
Se observa ca fiecare df are anumite coloane empty. sa se elimine acestea. '''

cars1 = pd.read_csv("cars1.csv")
cars2 = pd.read_csv("cars2.csv")


'''Numarul de observatii pentru fiecare df '''

print(len(cars1))
print(len(cars2))

'''Pentru cars1 sa se afiseze primele 7 coloane '''



'''Folosind iloc sa se afiseze toate coloanele, mai putin ultimele 3 '''

'''Sa se construiasca un singur df pornind de la cele doua seturi de date'''

'''Sa se citeasca setul de date fotbal.csv intr-un dataframe'''

'''Sa se afiseze echipele care au avut ma mult de 5 goluri '''

'''Sa se afiseze echipele care incep cu litera  R'''

'''Sa se afiseze valorile pentru Shooting Accuracy pentru Russia, Germany si Greece'''

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
