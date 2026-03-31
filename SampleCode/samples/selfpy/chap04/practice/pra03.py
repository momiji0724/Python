sum = 0
i = 1

while True:
    if i % 2 != 0:
        i += 1
        continue

    sum += i

    if i > 100:
        print(f'合計値は{sum}です。')
        break
    i += 1
