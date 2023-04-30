import datetime

data_waktu = datetime.datetime.now()
print(f"date time now\t: {data_waktu}")
print(f"tahun\t\t: {data_waktu.year}")
print(f"hari\t\t: {data_waktu.strftime('%A')}")

from collections import Counter

data = ["a", "b", "c", "d", "a", "d", "a" ]

# count = 0

# for i in data:
#     if i == "a":
#         count += 1

# print(count) 


# USING COUNTER
data_count = Counter(data)

print(f"data count\t: {data_count}")
print(f"jumlah a\t: {data_count['a']}")
print(f"jumlah d\t: {data_count['d']}")

import io

file = io.open("file_text.txt", "r")
print(file.read())
