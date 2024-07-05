# generar_reportes.py

import csv

def generar_reporte_equivalencia():
    # Supongamos que tienes datos de prueba
    resultados = [
        {'caso': 'Caso 1', 'resultado': 'Pasó'},
        {'caso': 'Caso 2', 'resultado': 'Falló'},
        {'caso': 'Caso 3', 'resultado': 'Pasó'},
    ]

    # Generar reporte CSV
    with open('pruebas_caja_N/reportes/reporte_equivalencia.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['caso', 'resultado'])
        writer.writeheader()
        writer.writerows(resultados)

    print("Reporte de equivalencia generado correctamente.")

def generar_reporte_valor_limite():
    # Supongamos que tienes más datos de prueba
    resultados = [
        {'caso': 'Caso 1', 'resultado': 'Falló'},
        {'caso': 'Caso 2', 'resultado': 'Pasó'},
        {'caso': 'Caso 3', 'resultado': 'Pasó'},
    ]

    # Generar reporte CSV
    with open('pruebas_caja_N/reportes/reporte_valor_limite.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['caso', 'resultado'])
        writer.writeheader()
        writer.writerows(resultados)

    print("Reporte de valor límite generado correctamente.")

# Ejemplo de uso
if __name__ == "__main__":
    generar_reporte_equivalencia()
    generar_reporte_valor_limite()
