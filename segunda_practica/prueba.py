from web_scraping_bolsa import scraping

df = scraping()


print(df)

# Ordena el DF de en forma descendiente según el valor
print("------- Df ordenado -------------------")
dfOrderValor = df.sort_values('Valor',ascending=False)
print(dfOrderValor)

# Imprime los dos máximos y dos mínimos
print("----- Los dos máximos valores son: -----")
print(dfOrderValor[:2])

print("----- Los dos mínimos valores son: -----")
print(dfOrderValor[-2:])


# Me imprime sólo el máximo y mínimo (no los dos)
maximo = df.max()
minimo = df.min()

print("Máximo-----------------")
print(maximo)
print("Mínimo-----------------")
print(minimo)