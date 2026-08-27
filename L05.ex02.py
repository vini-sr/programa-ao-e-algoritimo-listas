def contar_ois():
    contador = 0
    
    for i in range(1, 10):
        if i != 3:
            
            for j in range(1, 7):
                print('oi')
                contador += 1
                
    return contador


total = contar_ois()
print(f"Total de 'oi' impressos: {total}")
