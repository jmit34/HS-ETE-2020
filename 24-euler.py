def numerator(k):
    res = 1
    for j in range(1,k+1):
        res *= j
    return res

def denominator(k):
    res = 1
    for j in range(1,2*k+2,2):
        res *= j
    return res

n = 100
my_pi = 2

for i in range(1,n):
    my_pi += 2 * numerator(i) / denominator(i)

print(my_pi)
