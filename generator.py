# 1.
def sq_gen():
    x = 1
    while True:
        yield x**3
        x += 1

for n in sq_gen():
    if n > 1000:
        break
    print(n)


# 2. Pipeling
def gen_int(n):
    for i in range(n):
        yield i

def gen_2(gen):
    print(gen)
    for n in gen:
        if n % 2:
            yield n

for i in gen_2(gen_int(10)):
    print(i)