
# Funcții Lambda

X = lambda a: a + 10
print(X(10))

# Funcții
def myFunc(n):
    return lambda a: a*n # Putem folosi functii lambda in interiorul functiilor

doubler = myFunc(2)
print(doubler(5))
tripler = myFunc(3)
print(tripler(22))

my_list = [1,2,3,4,5,6]
result = list(map(lambda x: x ** 2, my_list))
print(result)

my_list2 = [2,4,6,8,10,11,12,14]
result2 = list(
    filter(lambda x:x%2==0, my_list2)
)
print(result2)


# Deschiderea unui fisier pentru citire (`r`)
file = open('example.txt','r')

# Deschiderea unui fisier pentru scriere (`w`)
file = open('example.txt','w')

# Deschiderea unui fisier pe modul append (`a`)
file = open('example.txt','a')

# Deschiderea unui fisier pentru citire si scriere (`r+`)
file = open('example.txt','r+')


# Citirea unui fisier intreg
file = open('example_2.txt','r')
content = file.read()
print(content)

file.seek(0) # Trebuie sa intoarcem cursorul la prima linie pentru a putea citi din nou
# Citirea unei linii din fisier
line = file.readline()
print(line)

# Citirea tuturor liniilor intr-o lista
lines = file.readlines()
print(lines)

file.close()

# Citirea din fisier
file = open('example123','w')
file.write('Hello,world!\n')
lines = ['First line\n','Second line\n']
file.writelines(lines)
file.close()

file= open('example123','r')
print(file.read())
