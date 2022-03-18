def sq_gen():
    x = 1
    while True:
        yield x**3
        x += 1

for n in sq_gen():
    if n > 1000:
        break
    print(n)
    