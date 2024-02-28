import itertools

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_prime_numbers(limit):
    primes = []
    for i in range(2, limit):
        if is_prime(i):
            primes.append(i)
    return primes

def min_containers(X):
    primes = get_prime_numbers(30)
    min_total_containers = float('inf')
    min_containers = None

    for combination in itertools.product(range(X+1), repeat=len(primes)):
        total_containers = sum(combination)
        total_liters = sum(c * p for c, p in zip(combination, primes))
        if total_liters == X and total_containers < min_total_containers:
            min_total_containers = total_containers
            min_containers = combination

    return min_containers

# Example usage:
X = 100
containers = min_containers(X)
primes = get_prime_numbers(30)
for i, container_count in enumerate(containers):
    if container_count > 0:
        print(f"Container {primes[i]} = {container_count} container(s)")
