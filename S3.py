help(print) # Afișează atât explicația funcției, cât și parametri posibili

x = 5
print(type(x)) # Totul in Python este un obiect. Astfel, fiecare tip de date este o clasa.

x = '1078'
print(type(x)) # Tipul variabilelor se poate schimba dinamic ( Dynamic Typing )

var = '2'
print(type(int(var))) # Conversia se face apeland constructorul acelei clase

var_f = 2.2
var_i = int(var_f)
print(var_i) # Se truncheaza numarul atunci cand trecem de la float la int


var_s = "Hello1078"
print(var_s[0]) # Sirurile de caractere pornesc numaratoarea caracterelor de la 0
print(var_s[-1]) # Daca punem "-" inaintea pozitiei, incepem numaratoarea de la coada la cap
print(var_s[0:5]) # Se preia intervalul pana ultimul caracter din acel interval,
# adica toate caracterele de la pozitia 0 la pozitia 4
print(var_s[:-2]) # Totul pana la antepenultimul caracter, deoarece numaratoarea se face invers doar pentru -2

nr_de_caractere = len(var_s) # Folosim len( ) pentru a determina nunarul de caractere dintr-un sir
print(nr_de_caractere)

print(var_s[5:len(var_s)]) # Ultimele 4 caractere din sir

# STRINGURILE IN PYTHON SUNT IMMUTABLE ( Nu se pot face atribuiri pe caracterele sirului )
# var_S[0]='b' FALS

print(var_s.find("1078")) # Metoda .find() returneaza inceptul secventei din sirul de caractere care se potriveste cu cea cautata
print(var_s.find("2759")) # Valoarea echivalenta pentru falsitate este -1

var_new = var_s.replace("1078","World") # Metoda .replace() creaza un sir nou de caractere cu secventa veche inlocuita cu cea introdusa
print(var_new)
var_s.replace("2064","World") # Lasa sirul asa cum era

b = 'a,b,c,d,e'
lista_de_caractere = b.split(',') # Metoda .split() returneaza O LISTA dupa separatorul introdus
print(lista_de_caractere[0]) # Returneaza primul element din lista creata

print(b.upper())

c = ' BAC '
print(c.lower()) # Transforma caracterele in minuscule
print(c.strip()) # Elimina spatiile
print(c.rstrip()) # Elimina doar spatiile de la final

d = b + c # Se pot concatena doua siruri cu operatorul +
print(d)

e = 1 + 2
print(e)

# LISTE

movies = ['M1','M2','M3','M4','M5']
print(len(movies)) # Se poate folosi functia len() si pentru lista

print(movies[3])
print(movies[2:5])
print(movies[1:4])

movies_1 = ['M6','M7']
movies_2 = movies + movies_1 # Putem concatena si liste in acelasi mod ca si sirurile de caractere
print(movies_2)

movies_2.append(5) # Putem folosi metoda .append() pentru a adauga un singur element la capatul listei
print(movies_2)

movies_2[2] = 'Titanic' # Cand folosim liste putem modifica elementele in parte ( mutable )
print(movies_2)

movies_2.pop(2) # Putem folosi metoda .pop() pentru a scoate un element specific din lista dupa pozitia acestuia
movies_2.pop() # Daca nu ii dam un parametru va scoate ultimul element din lista

movies_3 = ['M8','M9']
del(movies_3[0]) # Putem sterge din memorie un singur element din lista
del(movies_3) # Sau intreaga lista

movies_2.clear() # Metoda .clear() elibereaza lista dar nu o sterge de tot din memorie

# TUPLURI -- SUNT IMMUTABLE ( singura diferenta semnificativa fata de liste )

T = (1,2,2.3,'d',[1,2,3])
T_2 = (4, 5, 1, 2)
T_3 = T + T_2

print(T_3)

print(T_3.index('d'))
print(T_3.index(2))
print(T_3.count(2))

# SETURI -- NU AU DUPLICATE & SE POT FOLOSI FUNCTII SI METODE CA LA MANIPULAREA DE MULTIMI

set_var = {'a', 'b', 1, 5, 9}
print(set_var)  # Caracterele intr-un set apar de fiecare data in alta ordine

set_var = set("10781078")
print(set_var) # Se elimina toate caracterele duplicate si se imparte sirul de caractere in fiecare caracter specific

engineers = {'andrei', 'maria', 'ioana'}
managers = {'maria', 'sorin', 'dana'}

# Este Maria inginer?
print('maria' in engineers) # Returneaza un boolean care indica daca elementul a fost gasit in set sau nu

# Toti angajatii
print(engineers.union(managers))
print(engineers | managers)

# Cine este si inginer si manager
print(engineers & managers)
print(engineers.intersection(managers))

# Cine este inginer dar nu este manager
print(engineers - managers)
print(engineers.difference(managers))

# Sunt toti inginerii manageri?
print(managers.issuperset(engineers))
print(managers > engineers)

# Sunt David si Alina manageri?
print({'david','alina'}.issubset(managers))
print({'david','alina'} < managers)
