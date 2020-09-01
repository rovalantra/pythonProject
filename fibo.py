def fibonacci(a):
    prev = 0
    curr = 1
    for i in range(0, a):
        if i == 0:
            print(prev)
        else:
            print(curr)
            prev, curr = updatePrevAndCurr(curr, prev)


def updatePrevAndCurr(curr, prev):
    temp = curr
    curr = prev + curr
    prev = temp
    return prev, curr


fibonacci(100000000)
