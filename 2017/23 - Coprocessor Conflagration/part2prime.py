i = 107900

count = 0

while i <= 124900:
    prime = False
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime = True

    if not prime:
        count += 1
    i += 17

print(count)