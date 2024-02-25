Lugar_caminar = "Farallones del Citara"
Num_caminantes = 15
num_kms = 25.8
nivel_dificultad = 4.8
valor = 490000
print(Lugar_caminar)
print(Num_caminantes, " Personas")
print(num_kms, "Kms ")
print(nivel_dificultad, "Muy Exigente, aptas para personas expertas")
print(valor, "Pesos")
print()

for _ in range(5):
    nombre_caminate = input("Nombre del caminante: ")
    edad_caminante = int(input("Ingrese la edad del caminante: "))
    enfermedades_presentadas = input("Enfermedades presentadas por el caminante: ")
    enfermedades_cronicas = input("Si presenta alguna enfermedad, describir si es crónica: ")

    if edad_caminante >= 60 and enfermedades_cronicas == "si":
        print("Por favor, abstenerse de ir. El caminante", nombre_caminate, "tiene más de 60 años y presenta una enfermedad crónica.")
    elif enfermedades_cronicas == "si":
        print("El caminante", nombre_caminate, "presenta una enfermedad crónica. Favor consultar si es apto para esta actividad.")
    elif edad_caminante > 60:
        print("El caminante", nombre_caminate, "tiene más de 60 años pero goza de buena salud.")
    else:
        print("El caminante", nombre_caminate, "puede asistir sin restricciones.")




