
#Acest program ia trei nume de la user şi le scrie intr-un fisier
print('Introduceti numele a trei client:')
nume1 = input('Clientul 1 ')
nume2 = input('Clientul 2 ')
nume3 = input('Clientul 3 ')
#deschide un fisier numit clienti.txt
x = nume1+nume2+nume3
print(x)
fisier = open('clienti.txt', 'w')
#Scrie numele in fisier
fisier.write(nume1 + '\n')
fisier.write(nume2 + '\n')
fisier.write(nume3 + '\n')
#inchide fisierul
fisier.close()
print('Numele au fost scrise in clienti.txt')


#######

import pandas as pd
df = pd.DataFrame(
 {"Name": ["Braund, Mr. Owen Harris", "Allen, Mr. William Henry",
"Bonnell, Miss. Elizabeth"],
 "Age": [22, 35, 58],
 "Sex": ["male", "male", "female"]}
 )
print(df)

print("\n\n")

ages = pd.Series([22,35,58])
print(ages)

clienti_df = pd.read_csv('clienti_leasing20.csv')
print(clienti_df.iloc[2],'\n',type(df.iloc[2]))

