distancia_km = 225000000
#velocidad_kmh = 5000

for i in range(10000,50000,10000):
    tiempo_horas = distancia_km / i
    tiempo_dias = tiempo_horas / 24 
    print(f"velocidad: {i}km/h --> tiempos: {tiempo_dias} dias")