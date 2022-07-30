def gcd(a, b):
    val = 0
    for i in range(1,min(a, b)+1):
        if a % i == 0 and b % i == 0:
            val = i
    return int(val)
def lcm(a, b):
    value = gcd(a,b) * (a/gcd(a,b)) * (b/gcd(a,b))
    return int(value)
print(gcd(24,18))
print(lcm(24,18))