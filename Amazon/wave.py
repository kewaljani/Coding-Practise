arrive = [1, 3, 5]
depart = [2, 6, 8]
K = 1
events = [(t, 1) for t in arrive] + [(t, 0) for t in depart]
events = sorted(events)
print(events)
guests = 0

for event in events:
    if event[1] == 1:
        guests += 1
    else:
        guests -= 1

    if guests > K:
        print(0)

print(1)