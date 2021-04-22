# Acak
import time

'''
m > 0 (the modulus is positive),
0 < a < m (the multiplier is positive but less than the modulus),
0 ≤ b < m (the increment is non negative but less than the modulus), and
0 ≤ X0 < m (the seed is non negative but less than the modulus).
'''

def isGanjil(x):
    if x%2 == 0: return 1
    return 0

def randomizing(seed,a,b,n,m=11):
    hasil = []
    for i in range(n):
        seed = (a * seed + b) % m
        hasil.append(seed)
    return hasil

def random():
    mytime = str(time.process_time())
    rendem = isGanjil(int(mytime[len(mytime)-1]))
    hasil = randomizing(int(mytime[len(mytime)-1]),int(mytime[len(mytime)-2]),int(mytime[len(mytime)-2]),2)[rendem]
    print(hasil)

random()