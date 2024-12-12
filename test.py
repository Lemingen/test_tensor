import os
from alive_progress import alive_bar
path = "/Users/igorumaraliev/PyCharmProjects/new_test_tasks/test"

lib = {}
counter = []

def fun(path):
    lst = os.listdir(path)
    if lst:
        for i in lst:
            if '.' in i:
                extension = i.split('.')[-1]

                if extension in lib:
                    lib[extension] += 1
                else:
                    lib[extension] = 1

                counter.append(f"{path}/{i}")

            else:
                fun(path + "/" + i)

                if "dir" in lib:
                    lib["dir"] += 1
                else:
                    lib["dir"] = 1

                counter.append(f"{path}/{i}")

fun(path)

with alive_bar(len(counter)) as bar:
    for i in counter:
        if '.' in i:
            os.remove(i)
            bar()
        else:
            os.rmdir(i)
            bar()

for key, value in lib.items():
    print(f'Файл типа: .{key} был удалён: {value} раз(а)')