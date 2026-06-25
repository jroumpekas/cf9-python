my_list = [1, 2, 3, 4, 5] #list(range(1, 5))

a, b, c, d, e = my_list
print(f"Unpacked values: a={a}, b={b}, c={c}, d={d}, e={e}")

a, _, c, _, e = my_list
print(f"Unpacked values: a={a}, b={b}, c={c}, e={e}")

x, *rest =my_list
print(x)
print(rest)

*start, z = my_list
print(start)
print(z)

start, *middle, end = my_list
print(f"start: {start}")
print(f"middle: {middle}")
print(f"end:{end}")

my_list = [1, 2]

a, b, *rest = my_list
print(f"a: {a}")
print(f"b: {b}")
print(f"rest: {rest}")