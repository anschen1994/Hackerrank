def f(b,u0):
	while 1:
		yield u0
		u0 = 1e-9 * int(2**(b-u0**2))

b = 30
u0 = 0

a = f(b,u0)
for i in range(100):
	print(next(a))