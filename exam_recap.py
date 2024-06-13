
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
