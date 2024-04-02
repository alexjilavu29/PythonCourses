import pandas as pd
import matplotlib.pyplot as plt

'''Sa se incarce cele doua fisiere cars1/cars2 in dataframes.
Se observa ca fiecare df are anumite coloane empty. sa se elimine acestea. '''

cars1 = pd.read_csv("cars1_processed.csv")
cars2 = pd.read_csv("cars2_processed.csv")


'''Numarul de observatii pentru fiecare df '''

print(len(cars1))
print(len(cars2))
print(cars1)
print(cars2)
'''Pentru cars1 sa se afiseze primele 7 coloane '''

print(cars1.iloc[:,:7])

'''Folosind iloc sa se afiseze toate coloanele, mai putin ultimele 3 '''

print(cars1.iloc[:,:-3])

'''Sa se construiasca un singur df pornind de la cele doua seturi de date'''

cars_total = pd.concat([cars1, cars2], axis=0)

print(cars_total.head())

'''Sa se citeasca setul de date fotbal.csv intr-un dataframe'''

fb=pd.read_csv("fotbal.csv")
print(fb)

'''Sa se afiseze echipele care au avut mai mult de 5 goluri '''

print(fb.loc[fb["Goals"]>5])

'''Sa se afiseze echipele care incep cu litera  R'''

echipe_r = fb[fb["Team"].str.startswith('R')]
print(echipe_r)

'''Sa se afiseze valorile pentru Shooting Accuracy pentru Russia, Germany si Greece'''

print(fb.loc[fb["Team"].isin(["Russia","Germany","Greece"]),["Shooting Accuracy"]])

'''Sa se afiseze randurile //(de la al treilea la al saptelea)  de la 3 la 7 si coloanele de la 3 la 6'''

print(fb.iloc[2:7,2:6])

'''Sa se afiseze toate randurile pana la randul numarul 4 si toate coloanele'''

print(fb.iloc[:5,:])

'''Sa se stearga coloana -Players used-'''

fb_wo_players_used = fb.drop("Players Used",axis=1)
print(fb_wo_players_used)

'''Sa se stearga primele doua randuri '''

fb_wo_2 = fb.drop([0,1])
print(fb_wo_2)

'''Sa se citeasca setul de date drinks intr-un dataframe '''

drinks = pd.read_csv("drinks.csv")
with pd.option_context('display.max_columns', None):
    print(drinks)

'''Pe ce continent se consuma, in medie, mai multa bere? '''

print(drinks.loc[drinks["beer_servings"]==drinks["beer_servings"].max(),["country","beer_servings","continent"]])

'''afisati statisticile pentru consumul de vin '''

print(drinks.loc[:,["country","wine_servings"]])

'''Afisati media, mediana, minimul si maximul pentru consumul de bere pt fiecare continent'''

statistici = drinks.groupby('continent')['beer_servings'].agg(['mean', 'median', 'min', 'max'])
print(statistici)

'''Sa se afiseze o histograma a continentelor care consuma cea mai multa bere  '''

'''Sa se citeasca setul de date tips intr-un dataframe '''

'''Au fost mai multi clienti de gen masculin sau feminin?'''

'''pentru fiecare gen, sa se calculeze valoarea minima, valoarea maxima si media tip-ului acordat'''

'''pentru fiecare tip de masa (Dinner/Lunch) sa se calculeze procentul de clienti - barbati/femei'''

'''Sa se afiseze grafic top 5 cele mai mari note de plata '''

'''folosind while sa se calculeze media a 5 numere primite de la tastatura '''
