def contar_multiplos_14(inicio, fim):
    
    primeiro = inicio if inicio % 14 == 0 else inicio + (14 - (inicio % 14))
    
    multiplos = list(range(primeiro, fim + 1, 14))
    return len(multiplos)

print(contar_multiplos_14(1067, 3627))
