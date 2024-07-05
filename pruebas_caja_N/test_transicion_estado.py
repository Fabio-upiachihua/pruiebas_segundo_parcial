# pruebas_caja_N/test_transicion_estado.py

import unittest
from app import save_patient, load_patients, mark_medication_picked_up

class TestTransicionEstado(unittest.TestCase):
    
    def test_transicion_medication_picked_up(self):
        # Caso de prueba para transición de estado (recogida de medicación)
        patient_data = {
            'first_name': 'Luis',
            'last_name': 'Lopez',
            'age': 25,
            'dni': '45678901',
            'patient_number': 'P005',
            'insured': True
        }
        save_patient(patient_data)

        mark_medication_picked_up(patient_data['patient_number'])

        patients = load_patients()
        for patient in patients:
            if patient['patient_number'] == patient_data['patient_number']:
                self.assertTrue(patient['medication_picked_up'])
                break
        else:
            self.fail('No se encontró el paciente')

    # Agregar más casos de prueba según transiciones de estado

if __name__ == '__main__':
    unittest.main()
