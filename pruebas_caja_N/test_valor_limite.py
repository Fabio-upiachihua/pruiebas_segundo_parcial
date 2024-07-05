# pruebas_caja_N/test_valor_limite.py

import unittest
from app import save_patient, load_patients, mark_medication_picked_up

class TestValorLimite(unittest.TestCase):
    
    def test_valor_limite_edad(self):
        # Caso de prueba para valor límite de edad
        # Caso 1: Edad mínima (18 años)
        patient_data = {
            'first_name': 'Pedro',
            'last_name': 'Ramirez',
            'age': 18,
            'dni': '23456789',
            'patient_number': 'P003',
            'insured': True
        }
        self.assertTrue(save_patient(patient_data))

        patients = load_patients()
        self.assertIn(patient_data, patients)

        # Caso 2: Edad máxima (65 años)
        patient_data = {
            'first_name': 'Ana',
            'last_name': 'Martinez',
            'age': 65,
            'dni': '34567890',
            'patient_number': 'P004',
            'insured': False
        }
        self.assertTrue(save_patient(patient_data))

        patients = load_patients()
        self.assertIn(patient_data, patients)

    # Agregar más casos de prueba según los valores límite

if __name__ == '__main__':
    unittest.main()
