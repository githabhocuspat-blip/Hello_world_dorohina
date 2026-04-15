n = [10, 20, 30, 40, 50, 60]
s = 0
count = 0
for i in range(len(n)):
    if i % 2 == 0:
        s = s + arr[i]
        count = count + 1
res = s / count
print("Среднее элементов с четными индексами:", res)
