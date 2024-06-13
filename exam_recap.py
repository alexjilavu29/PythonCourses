
# for i in range (0.5,5.5,0.5):
#     print(i)
# Variabilele sunt de tip float, deci trebuie sa folosim float in loc de int in functia range

a = (1,2,(4,5))
b = (1,2,(3,5))
a=b
print(a)
# Variabilele sunt de tip tuple, deci se pot atribui valorile intre ele
if a == b:
    print("True")
else:
    print("False")
# Variabilele se pot compara intre ele, deoarece sunt de tip tuple


# În funcție de amplasarea soluției Cloud, soluțiile Cloud pot fi:
# - Public Cloud
# - Private Cloud
# - Hybrid Cloud
# - Community Cloud

x = 0
for i in range(10):
    for j in range(-1, -10, -1):
        x += 1
        print(x)

t=(1,2,4,3,8,9)
ex = [t[i] for i in range(0, len(t), 2)]
print(ex)

n = 12345
s1 = 0
s2 = 0
while n!=0:
    if n%2==0:
        s1+=1
    else:
        s2+=1
    n//=10
print(s1,s2)

n = 7
count_n = 0
for i in range(1,n+1):
    for j in range(1,i):
        count_n+=1
        print(i,j)
print(count_n)


def f(value, values, ex_set):
    value=1
    values[0] = 44
    ex_set.pop()
t= 3
v = [1,2,3]
s = {1,2,3}
f(t,v,s)
print(t, v[0],s)