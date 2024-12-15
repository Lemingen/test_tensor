from datetime import datetime
lib=[]

with open('logs.txt', 'r') as file_logs:
    for line in file_logs:
        lst=line.split("|")
        lib.append(lst)

date_format = "%d.%m.%Y %H:%M:%S"
stat=[]
for i in lib[1:]:

    date_start = i[0].strip()
    date_end = i[1].strip()

    date1 = datetime.strptime(date_start, date_format)
    date2 = datetime.strptime(date_end, date_format)
    difference = date2 - date1
    difference_in_seconds = difference.total_seconds()
    stat.append(difference_in_seconds)

def find_median(stat):
    sorted_stat = sorted(stat)
    n = len(sorted_stat)

    if n % 2 == 1:
        median = sorted_stat[n // 2]
    else:
        mid1 = sorted_stat[n // 2 - 1]
        mid2 = sorted_stat[n // 2]
        median = (mid1 + mid2) / 2

    return median

count = 0
for i in lib[1:]:
    if int(i[3]) >= 400 or 'error' in (i[4]):
        count += 1

lib1={}
for i in lib[1:]:
    m = i[2].strip()
    if m in lib1:
        lib1[m] += 1
    else:
        lib1[m] = 1

print(f"Минимальное время обработки запроса = {min(stat)} секунд")
print(f"Максимальное время обработки запроса = {max(stat)} секунд")
print(f"Среднее арифметическое = {sum(stat)/ len(stat)} секунд")
print(f"Медианное значение = {find_median(stat)} секунд")
print(f"Процент ошибочных запросов = {(count/ (len(lib)-1)) * 100}%")
print()
for key, value in lib1.items():
    print(f'Локация: {key}, число вызовов: {value}')
