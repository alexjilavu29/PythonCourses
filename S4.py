x_dict = {
    "name": "Student 1",
    "age": 21,
    "courses": ["BD","POO","PS","Macroeconomie"]
}

print(x_dict.keys())
print(x_dict.values())
print(x_dict.items())
x_dict.update({"nota":10})
print(x_dict)

x_dict.pop("courses")
print(x_dict)
x_dict.popitem()
print(x_dict)

x = 1
if x:
    y = 2
    print(y)
    if y:
        print("block 2")
    print("block 1")
print("block 0")

# nr = input("Dati un numar: ")
# if int(nr) == 10:
#     print("Ai ghicit")
# else:
#     print("N-ai ghicit")

a = 0
b = 10
while a < b:
    print(a, end=' ')
    a += 1

print("\n")

x = 10
while x:
    x = x - 1
    if x % 2 != 0: continue
    print(x, end=' ')


print("\n")

x = 10
while x:
    x = x - 1
    if x % 2 == 0: break
    print(x, end=' ')

x = ['pizza', 'cheese', 'ham']
for food in x:
    print(food)

