def calcular_total():
    try:
        p1 = float(input("valor do primeiro produto: "))
        
        p2 = float(input("valor do segundo produto: "))

        print(f"Valor total da compra: R$ {p1 + p2:.2f}")

    except ValueError:
        print("Falha: os preços devem ser em numeros inteiros.")

calcular_total()
