import os
from traceback import print_tb

path1 = "/Users/igorumaraliev/PyCharmProjects/new_test_tasks/var/data1"
path2 = "/Users/igorumaraliev/PyCharmProjects/new_test_tasks/var/data2"
lst_arch = []
def fun(path1):
    lst = os.listdir(path1)
    for i in lst:
        if os.path.isdir(f"{path1}/{i}"):
            fun(path1 + "/" + i)
        else:
            lst_arch.append(f"{path1}/{i}")

fun(path1)

parts = []
for i in lst_arch:
    part = i.split('/')
    temp = part[7]
    part[7] = part[8]
    part[8] = temp
    temp = part[10]
    prom = temp.split('_', 2)
    lst = prom[-1].split('.')
    part[-1] = (f"{prom[1]}_{lst[0]}")
    part.append(f"{prom[0]}.{lst[1]}")
    part.pop(0)
    parts.append(part)

print(parts)

def make(path2):
    for i in parts:
        path2_save = path2
        for j in range(6, 11):
            path2 += "/"
            path2 += i[j]

            if i[j].count('.') == 1:
                with open(path2, 'w', encoding='utf-8') as file:
                    file.write('')
                print(f"{path2} создаю файл")

            elif not os.path.exists(path2):
                print(f"Папка ещё '{path2}' не уже существует. Создаю.")
                os.makedirs(path2)

            else:
                print(f"Папка '{path2}' уже существует.")
        path2 = path2_save

make(path2)