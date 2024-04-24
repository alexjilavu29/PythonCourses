import pandas as pd
import matplotlib.pyplot as plt

#Setul de date articles.csv contine informatii legate de articolele vandute in magazinele H&M.
customers = pd.read_csv("customers.csv")
print(customers.head().to_string())

#1.	Sa se afiseze numarul de cumparatori din fiecare categorie a coloanei 'fashion_news_frequency'.
# Rezultatul va contine numarul cumparatorilor doar pentru coloana ‘customer_id’, restul coloanelor vor fi ignorate.
print(customers.groupby('fashion_news_frequency')['customer_id'].count().to_string())

freq_group=customers.groupby('fashion_news_frequency')
print(freq_group.head().to_string())


# Verificare daca coloana 'customer_id' contine valori unice.

print(customers['customer_id'].is_unique)
# Pentru fiecare tip de frecventa se va calcula numarul de cumparatori unici.
print(customers.groupby('fashion_news_frequency')['customer_id'].nunique().to_string())


#Sa se reprezinte grafic rezultatul printr-un grafic tip barplot.
# Pentru fiecare grup de frecventa in parte:
customers.groupby('fashion_news_frequency')['customer_id'].count().plot(kind='bar')
plt.show()
# Pentru toti cumparatorii in ansamblu:
customers.plot(x='fashion_news_frequency',  kind='bar')
plt.show()


#2.	Sa se modifice setul de date initial astfel incat pentru observatiile ce contin valoarea 'None' sau 'NONE' in coloana 'fashion_news_frequency' sa apara valoarea 'Missing'.
customers['fashion_news_frequency'] = customers['fashion_news_frequency'].replace(['None', 'NONE'], 'Missing')
print(customers['fashion_news_frequency'].value_counts().to_string())