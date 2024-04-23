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

# axis = 0 reprezinta faptul ca se concateneaza raportat la directia de linii


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

print(fb.iloc[2:7,2:6])

'''Sa se afiseze toate randurile pana la randul numarul 4 si toate coloanele'''

print(fb.loc[:"4",:])

'''Sa se stearga coloana -Players used-'''

fb2 = fb.drop("Players Used", axis=1)
print(fb2)

# fb.drop() este folosit pentru a scoate o coloana din dataframe

'''Sa se stearga primele doua randuri '''

print(fb2.drop([0,1]))

'''Sa se citeasca setul de date drinks intr-un dataframe '''

drinks = pd.read_csv("drinks.csv")
print(drinks.to_string())

'''Pe ce continent se consuma, in medie, mai multa bere? '''

print(drinks.loc[drinks["beer_servings"]==drinks["beer_servings"].max(),["continent","beer_servings"]])

'''afisati statisticile pentru consumul de vin '''

print(drinks["wine_servings"].describe())

'''Afisati media, mediana, minimul si maximul pentru consumul de bere pt fiecare continent'''

print(drinks["beer_servings"].agg(["mean","min","max"]))


import seaborn as sns

'''Sa se afiseze o histograma a continentelor care consuma cea mai multa bere  '''
# Sa se afiseze o histograma a continentelor care consuma cea mai multa bere
# Se grupeaza dupa continent si se calculeaza suma de bere servita
# Se sorteaza valorile in ordine descrescatoare
# Se afiseaza un grafic de tip barplot
# Se afiseaza graficul
db = drinks.groupby('continent')['beer_servings'].sum().sort_values(ascending=False)
sns.barplot(x=db.index, y=db.values)
plt.show()

cont_beer = drinks.groupby('continent')['beer_servings'].sum().sort_values(ascending=False)
#sns.pairplot(drinks,vars=['continent','beer_servings'],hue='PRESCORING',diag_kind='hist')
#plt.show()

'''Sa se citeasca setul de date tips intr-un dataframe '''

tips = pd.read_csv("tips.csv")
print(tips)

'''Au fost mai multi clienti de gen masculin sau feminin?'''

print(tips["gender"].value_counts())
#print(tips.groupby(''))

'''pentru fiecare gen, sa se calculeze valoarea minima, valoarea maxima si media tip-ului acordat'''

print(tips.groupby("gender")["tip"].agg(["min","max","mean"]))

'''pentru fiecare tip de masa (Dinner/Lunch) sa se calculeze procentul de clienti - barbati/femei'''
print("\n\n--------------------------------------------\n\n")
counts = tips.groupby(["time","gender"]).size()
print(counts)
print(counts.groupby("time").sum())
print((counts/(counts.groupby("time").sum()))*100)
print("\n\n--------------------------------------------\n\n")



print(tips.groupby("time")["gender"].value_counts())
counts = tips.groupby(["time","gender"]).size()
totalpertime = counts.groupby("time").sum()
print(totalpertime)
print(counts/totalpertime)

'''Sa se afiseze grafic top 5 cele mai mari note de plata '''

print(tips.sort_values(by="total_bill", ascending=False).head())
top_bills = tips.sort_values(by="total_bill", ascending=False).head()

# Folosind matplotlib.pyplot
plt.bar(top_bills.index, top_bills["total_bill"])
plt.show()

# Folosind seaborn
sns.barplot(x=top_bills.index, y=top_bills["total_bill"])
plt.show()


'''folosind while sa se calculeze media a 5 numere primite de la tastatura '''

i=0
sum=0
while i<5:
    x=input("Inserati un numar:")
    sum+=(int)(x)
    i+=1
print(sum)




# Siruri de caractere "..." '...'
# .find(" ") -> cauta o secventa intr-un sir
# .replace("old", "new") -> suprascrie un sir vechi cu unul nou
# .split("separator") -> imparte sirul intr-o lista dupa acel separator
# .lower() -> face toate caracterele minuscule
# .strip() -> sterge toate spatiile
# rstrip() -> sterge toate spatiile de la final


# Functii
# def functie( ... , ... ):
# return ...

# Functii LAMBDA -- functii care pot fi definite pentru a putea fi atribuite unor variabile sau folosite in alte functii
# lambda a : a + 10 -> daca se atribuie unei variabila, acea variabila devine o functie care ia un parametru si il incrementeaza cu 10
# Functiile lambda pot avea mai multe argumente in antet, insa urmeaza aceeasi sintaxa lambda a,b: a+b


# Liste [...]
# .append() -> adaugare element la finalul listei
# .pop() -> eliminare ultimul element din lista
# .pop(pozitie) -> eliminarea unui element specific in functie de pozitie
# len() -> lungimea listei
# lista1 + lista2 -> concatenare
# del(lista) -> sterge lista
# del(lista[i]) -> sterge elementul de pe pozitia i
# .clear() -> elimina toate elementele din lista
# range(n) -> de la 0 pana la n exclusiv
# range(a,k) -> de la a la k exclusiv k

# Tupluri (...) - immutable
# t1+t2 -> concatenare
# .index("...") -> indexul unui anumit element din tuplu
# .count("...") -> de cate ori apare un element anume

# Seturi {...} - no duplicates
# set("...") -> se elimina toate duplicatele si se creeaza un set cu caracterele ramase
# "..." in set1 -> True daca se gasesc elementul in set
# set1 | set2 -> reuniune de seturi
# set1 & set2 -> intersectie de seturi
# set1 - set2 -> ce e in set1 dar nu in set2
# set1 > set2 -> daca toate elementele din set2 sunt si in set1
# set1 < set2 -> daca toate elementele din set1 sunt si in set2

# Dictionare {... : ...}
# .keys() -> toate cheile din acel dictionar
# .values() -> toate valorile din acel dictionar
# .items() -> toate perechile cheie:valoare din acel dictionar
# .update({... : ...}) -> se modifica valoarea de la cheia indicata in cea noua
# .pop("...") -> se elimina cheia indicata
# .popitem() -> se elimina ultimul item din dictionar
# for i in dictionar -> parcurge toate itemele dictionarului
# list(df1.keys()) -> se preiau toate cheile si se adauga intr-o lista
# df1[cheie] -> returneaza valoarea de la acea cheie


# PANDAS - import pandas as pd
# from pandas import DataFrame -> ca sa nu mai scriem DataFrame. inainte de orice metoda
# from pandas import Series -> la fel pentru serii

# Series - similar cu dictionarele
# Series([...], index=[...]) -> Se creeaza o serie cu valori si indecsi indicati
# .values -> toate valorile
# .index -> toti indecsii
# pd.isna(serie) -> daca exista valori nule
# Series({... : ...}) -> transformare din dictionar in serie
# pd.notnull(serie) -> daca seria nu e nula

# DataFrame
# DataFrame( data = [ [...], [...], ..., [...] ] , index = [...] , columns = [...] , dtype = ... ) -> definire data frame cu nume pentru linii si coloane + data types
# .iloc(...,...) -> cautare dupa pozitia in data frame
# .head() -> primele 5 valori
# .head(n) -> primele n valori
# .tail(n) -> ultimele n valori


# Lucrul cu fisiere
# open(" ... .txt ", "r") -> deschidere pentru citire
# content = fisier.read() -> poate fi atribuit si parcurs continutul
# fisier.readline() -> se citeste cate o linie
# fisier.readlines() -> se citesc mai multe linii deodata
# fisier.close()

