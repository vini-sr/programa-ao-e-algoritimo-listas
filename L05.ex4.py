def questao_d(inicio=18644, fim=33087):
    total = 0
    for n in range(inicio, fim + 1):
        s = str(n)
        if '2' in s and '7' not in s:
            total += 1
    return total

print(f"Total: {questao_d()}")
