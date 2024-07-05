# generar_graficos.py

import matplotlib.pyplot as plt

def generar_grafico_valor_limite():
    # Datos de ejemplo para gráfico de barras
    casos = ['Caso 1', 'Caso 2', 'Caso 3']
    resultados = [10, 15, 5]

    plt.bar(casos, resultados)
    plt.xlabel('Casos de Prueba')
    plt.ylabel('Resultados')
    plt.title('Resultados de Pruebas de Valor Límite')
    plt.savefig('pruebas_caja_N/reportes/resultados_valor_limite.png')  # Guarda el gráfico como imagen
    plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    generar_grafico_valor_limite()
