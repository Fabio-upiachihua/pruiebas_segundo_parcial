# pruebas_caja_N/test_equivalencia.py

import unittest
from app import save_patient, load_patients, mark_medication_picked_up

class TestEquivalencia(unittest.TestCase):
    
    def test_equivalencia_edad(self):
        # Caso de prueba para partición de equivalencia de edad
        # Caso 1: Edad válida (entre 18 y 65 años)
        patient_data = {
            'first_name': 'Juan',
            'last_name': 'Perez',
            'age': 30,
            'dni': '12345678',
            'patient_number': 'P001',
            'insured': True
        }
        self.assertTrue(save_patient(patient_data))

        patients = load_patients()
        self.assertIn(patient_data, patients)

    def test_equivalencia_dni(self):
        # Caso de prueba para partición de equivalencia de DNI
        # Caso 1: DNI válido (8 dígitos)
        patient_data = {
            'first_name': 'Maria',
            'last_name': 'Gonzalez',
            'age': 45,
            'dni': '87654321',
            'patient_number': 'P002',
            'insured': False
        }
        self.assertTrue(save_patient(patient_data))

        patients = load_patients()
        self.assertIn(patient_data, patients)

    # Agregar más casos de prueba según la partición de equivalencia

if __name__ == '__main__':
    unittest.main()
