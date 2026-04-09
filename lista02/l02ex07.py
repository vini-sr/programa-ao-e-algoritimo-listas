

area = float(input("Área a ser pintada (m²): "))
litros_necessarios = area / 3

latas = math.ceil(litros_necessarios / 18)
preco_total = latas * 80.00

print(f"Você precisará de {latas} latas.")
print(f"Preço total: R$ {preco_total:.2f}")
