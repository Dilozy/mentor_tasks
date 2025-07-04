def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

counter = make_counter()
print(counter())
print(counter())

counter2 = make_counter()
print(counter2())


def make_adder(start):
    total = start
    def adder(num):
        nonlocal total
        total += num
        return total
    return adder


adder = make_adder(10)
print(adder(5))