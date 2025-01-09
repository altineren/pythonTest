
def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def findPrimesStartingWith5():
    primes = []
    for num in range(500, 600):
        if isPrime(num):
            primes.append(num)
    return primes

if __name__ == "__main__":
    primes = findPrimesStartingWith5()
    print("Three-digit prime numbers starting with 5:", primes)