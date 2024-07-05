# pruebas_caja_N/test_tablas_decision.py

import unittest
from app import save_patient, load_patients, mark_medication_picked_up

class TestTablasDecision(unittest.TestCase):
    
    def test_tablas_decision(self):
        # Caso de prueba para tablas de decisión (ejemplo básico)
        patient_data = {
            'first_name': 'Sofia',
            'last_name': 'Gomez',
            'age': 50,
            'dni': '56789012',
            'patient_number': 'P006',
            'insured': False
        }
        save_patient(patient_data)

        # Simular condiciones que deben cumplirse según la tabla de decisión
        if patient_data['age'] >= 18 and patient_data['insured']:
            mark_medication_picked_up(patient_data['patient_number'])

        patients = load_patients()
        for patient in patients:
            if patient['patient_number'] == patient_data['patient_number']:
                self.assertEqual(patient['medication_picked_up'], True)
                break
        else:
            self.fail('No se encontró el paciente')

    # Agregar más casos de prueba según las tablas de decisión

if __name__ == '__main__':
    unittest.main()
