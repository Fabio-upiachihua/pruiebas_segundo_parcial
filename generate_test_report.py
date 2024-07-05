# pruebas_caja_N/generate_test_report.py

import pandas as pd
import matplotlib.pyplot as plt
import unittest
import os

# Importar los módulos de prueba
import test_equivalencia
import test_valor_limite
import test_transicion_estado
import test_tablas_decision

# Función para ejecutar las pruebas y recopilar resultados
def run_tests():
    loader = unittest.TestLoader()
    tests = [
        loader.loadTestsFromModule(test_equivalencia),
        loader.loadTestsFromModule(test_valor_limite),
        loader.loadTestsFromModule(test_transicion_estado),
        loader.loadTestsFromModule(test_tablas_decision)
    ]
    suite = unittest.TestSuite(tests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return result

# Función para generar el reporte en DataFrame
def generate_report(result):
    data = {
        "Test": [],
        "Resultado": [],
        "Errores": [],
        "Fallos": []
    }
    for test, error in result.errors:
        data["Test"].append(str(test))
        data["Resultado"].append("Error")
        data["Errores"].append(error)
        data["Fallos"].append("")

    for test, failure in result.failures:
        data["Test"].append(str(test))
        data["Resultado"].append("Fallo")
        data["Errores"].append("")
        data["Fallos"].append(failure)

    for test in result.testsRun:
        if str(test) not in data["Test"]:
            data["Test"].append(str(test))
            data["Resultado"].append("Exitoso")
            data["Errores"].append("")
            data["Fallos"].append("")

    df = pd.DataFrame(data)
    return df

# Función para generar gráficos
def generate_graphs(df):
    result_counts = df['Resultado'].value_counts()
    
    plt.figure(figsize=(10, 6))
    result_counts.plot(kind='bar', color=['green', 'red', 'orange'])
    plt.title('Resultados de las Pruebas')
    plt.xlabel('Resultado')
    plt.ylabel('Cantidad')
    plt.savefig('pruebas_caja_N/test_results.png')

    plt.show()

# Ejecutar las pruebas y generar el reporte
if __name__ == '__main__':
    result = run_tests()
    df = generate_report(result)
    print(df)
    df.to_csv('pruebas_caja_N/test_report.csv', index=False)
    generate_graphs(df)
