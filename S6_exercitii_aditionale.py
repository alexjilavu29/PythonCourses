import pandas as pd
import matplotlib.pyplot as plt

'''Sa se incarce cele doua fisiere cars1/cars2 in dataframes.
Se observa ca fiecare df are anumite coloane empty. sa se elimine acestea. '''

cars1 = pd.read_csv("cars1_processed.csv")
cars2 = pd.read_csv("cars2_processed.csv")

cars11 = pd.read_csv("cars1.csv",sep=",")
print(cars11)

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

consum_bere_continent = drinks.groupby('continent')['beer_servings'].sum().sort_values(ascending=False)

consum_bere_continent.plot(kind='bar', color='skyblue')

plt.title('Consumul Total de Bere pe Continente')
plt.xlabel('Continent')
plt.ylabel('Consum Total de Bere')
plt.xticks(rotation=45)

plt.show()

'''Sa se citeasca setul de date tips intr-un dataframe '''

tips = pd.read_csv("tips.csv")
print(tips)

'''Au fost mai multi clienti de gen masculin sau feminin?'''

if tips["gender"].value_counts()["Female"] > tips["gender"].value_counts()["Male"]:
    print("Mai multi clienti de gen feminin")
elif tips["gender"].value_counts()["Female"] < tips["gender"].value_counts()["Male"]:
    print("Mai multi clienti de gen masculin")
else:
    print("Sunt la fel de multi clienti de gen masculin si feminin")

'''pentru fiecare gen, sa se calculeze valoarea minima, valoarea maxima si media tip-ului acordat'''

stat_tip = tips.groupby('gender')['tip'].agg(['min','max','mean'])
print(stat_tip)

'''pentru fiecare tip de masa (Dinner/Lunch) sa se calculeze procentul de clienti - barbati/femei'''

grupat = tips.groupby(['time', 'gender']).size().reset_index(name='counts')
print(grupat)
total_per_time = grupat.groupby('time')['counts'].transform('sum')
print(total_per_time)
grupat['percentage'] = (grupat['counts'] / total_per_time) * 100
print(grupat)

'''Sa se afiseze grafic top 5 cele mai mari note de plata '''

top_5_note = tips.sort_values(by='total_bill', ascending=False).head(5)

plt.figure(figsize=(10, 6))
plt.bar(top_5_note.index, top_5_note['total_bill'], color='skyblue')
plt.title('Top 5 Cele Mai Mari Note de Plată')
plt.xlabel('Indexul Notelor de Plată')
plt.ylabel('Valoarea Notei de Plată')
plt.xticks(top_5_note.index)
plt.show()

'''folosind while sa se calculeze media a 5 numere primite de la tastatura '''

media = 0
i = 1
while i != 6 :
    media += (int)(input(f"Inserati numarul {i}:"))
    i+=1
media/=5
print(f"Media celor 5 numere introduse este {media}")