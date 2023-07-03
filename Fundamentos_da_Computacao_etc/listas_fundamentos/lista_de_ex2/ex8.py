etat_a = 5000000
pays_b = 7000000
birth_rate_a = 0.03
birth_rate_b = 0.02
anos = 0
while etat_a <= pays_b:
    etat_a += etat_a * birth_rate_a
    pays_b += pays_b * birth_rate_b
    anos += 1
print(f"Serão necessários {anos} anos para que a população do estado A ultrapasse a população do país B.")