import matplotlib.pyplot as plt

def generar_grafico_porcentajes():
    # Datos de ejemplo para gráfico de barras
    pruebas = ['Part. Equivalencia', 'Valor Límite', 'Trans. Estado', 'Tablas Decisión']
    porcentajes = [80, 85, 75, 90]  # Porcentajes ficticios para el ejemplo

    plt.bar(pruebas, porcentajes, color=['blue', 'green', 'red', 'purple'])
    plt.xlabel('Tipos de Prueba')
    plt.ylabel('Porcentaje de Éxito')
    plt.title('Porcentajes de Éxito por Tipo de Prueba')
    plt.ylim(0, 100)  # Limitar el eje y de 0 a 100
    plt.savefig('porcentajes_exitos.png')  # Guardar el gráfico como imagen
    plt.show()

if __name__ == "__main__":
    generar_grafico_porcentajes()
