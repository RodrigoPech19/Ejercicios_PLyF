from functools import reduce

ventas_pesos_mx = [
    1500,
    2500,
    3200,
    4500,
    6000,
    1200,
    8000
]

precio_dolar = 20.46

#Calcula el promedio por dia de las ventas en pesos mexicanos.
promedio_ventamx = reduce(lambda total, x: total + x, ventas_pesos_mx) / len(ventas_pesos_mx)

#Convierte cada venta de pesos a dolares
ventas_mx_a_usd = list(map(lambda x: x / precio_dolar, ventas_pesos_mx))

#Filtra las ventas que superan los 150 dolares
ventas_superiores_filtradas = list(filter(lambda x: x > 150, ventas_mx_a_usd))

#Caalcula el total de las ventas filtradas
total_filtrado = reduce(lambda total, x: total + x, ventas_superiores_filtradas)

#imprime resultados
print(f"Promedio de ventas en pesos mexicanos: {promedio_ventamx:.2f}")
print(f"Ventas en dólares: {ventas_mx_a_usd}")
print(f"Ventas mayores a 150 dólares: {ventas_superiores_filtradas}")
print(f"Suma total de ventas mayores a 150 dólares: {total_filtrado:.2f}")

