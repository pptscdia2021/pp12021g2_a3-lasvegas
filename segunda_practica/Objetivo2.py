import 

def maxYMin():

    # Ordena el DF de en forma descendiente según el valor
    print("------- Df ordenado -------------------")
    dfOrderValor = df.sort_values('Valor',ascending=False)
    print(dfOrderValor)

    # Imprime los dos máximos y dos mínimos
    print("----- Los dos máximos valores son: -----")
    max = dfOrderValor[:2]
    print(max)

    print("----- Los dos mínimos valores son: -----")
    min = dfOrderValor[-2:] 
    print(min)

    # Me imprime sólo el máximo y mínimo (no los dos)
    maximo = df.max()
    minimo = df.min()

    print("Máximo-----------------")
    print(maximo)
    print("Mínimo-----------------")
    print(minimo)

    return(max, min, maximo, minimo)