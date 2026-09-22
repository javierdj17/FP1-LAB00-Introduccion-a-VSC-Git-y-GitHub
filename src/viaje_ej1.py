distancia_km = 384400  # distancia Tierra - Luna
velocidad_kmh = 5000
tiempo_horas = distancia_km // velocidad_kmh
tiempo_dias = tiempo_horas // 24
print(f"Tardarías {tiempo_dias} días en llegar.")

#se muestran numeros decimales en la primera opción ya que la operación / nos devuelve una división EXACTA con sus numeros decimales,
#mientras que la operación // nos devuelve solo la parte entera de esa división.