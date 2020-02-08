import time

# diverse manieren op fibonacci te berekenen
# 1, 1, 2, 3, 5, 8, 13, 21, etc

# met een for-lus
def fibf(n):
    previous = 1
    current = 1
    for i in range(1,n):
        previous, current = current, previous+current
    return current

# met een while-lus
def fibw(n):
    previous = 1
    current = 1
    i = 1
    while i < n:
        previous, current = current, previous+current
        i += 1
    return current

# met recursie
def fibr(n):
    if n < 2: return 1
    return fibr(n-1) + fibr(n-2)

def timer(func, n):
    start = time.time()
    func(n)
    end = time.time()
    return end-start

n = 34
print('Timing {:.9f} seconds'.format(timer(fibf,n)))
print('Timing {:.9f} seconds'.format(timer(fibw,n)))
print('Timing {:.9f} seconds'.format(timer(fibr,n)))