def sayHi(n, func):
    print("Hi " + n)
    func(n, func)


def sayBye(a, f):
    print("Bye " + a)
    f(a, f)


print(sayHi("world", sayBye))
