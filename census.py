import matplotlib.pyplot as plt
import numpy as np
import csv

results = []
dates = []
values = []

with open("census.csv") as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    for row in reader:
        dates.append(row[0])
        values.append(int(row[1]))

plt.bar(dates, values)
plt.xticks(rotation=45)
plt.show()
