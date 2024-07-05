import pandas as pd

def generar_reporte_particion_equivalencia():
    # Aquí se simulan datos para el ejemplo
    casos = ['Caso 1', 'Caso 2', 'Caso 3']
    resultados = ['Pasa', 'Pasa', 'Falla']
    df = pd.DataFrame({'Caso': casos, 'Resultado': resultados})
    df.to_csv('reporte_particion_equivalencia.csv', index=False)

def generar_reporte_valor_limite():
    # Aquí se simulan datos para el ejemplo
    casos = ['Caso 1', 'Caso 2', 'Caso 3']
    resultados = ['Pasa', 'Pasa', 'Falla']
    df = pd.DataFrame({'Caso': casos, 'Resultado': resultados})
    df.to_csv('reporte_valor_limite.csv', index=False)

def generar_reporte_transicion_estado():
    # Aquí se simulan datos para el ejemplo
    casos = ['Caso 1', 'Caso 2']
    resultados = ['Pasa', 'Falla']
    df = pd.DataFrame({'Caso': casos, 'Resultado': resultados})
    df.to_csv('reporte_transicion_estado.csv', index=False)

def generar_reporte_tablas_decision():
    # Aquí se simulan datos para el ejemplo
    casos = ['Caso 1', 'Caso 2']
    resultados = ['Pasa', 'Falla']
    df = pd.DataFrame({'Caso': casos, 'Resultado': resultados})
    df.to_csv('reporte_tablas_decision.csv', index=False)

if __name__ == "__main__":
    generar_reporte_particion_equivalencia()
    generar_reporte_valor_limite()
    generar_reporte_transicion_estado()
    generar_reporte_tablas_decision()
    print("Reportes generados correctamente.")
