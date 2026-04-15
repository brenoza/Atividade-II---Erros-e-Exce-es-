def calcular_media():
    notas = []
    
    for i in range(3):
        try:

            nota = float(input("escreva a sua nota: "))
            notas.append(nota)

        except ValueError:

            print("Falha: as notas devem ser em numeros inteiros.")
            return
    
    media = sum(notas) / 3
    print(f"A sua media final: {media:.2f}")

calcular_media()
