is_prime = [True]*150
is_prime[0] = False
is_prime[1] = False

primes = []

for num in range(2, 150):
    if not is_prime[num]:
        continue
    
    primes.append(num)

    for not_prime in range(num*2, 150, num):
        is_prime[not_prime] = False

target = int(input())

for idx, val in enumerate(primes):
    if target < (answer:=val*primes[idx+1]):
        print(answer)
        break