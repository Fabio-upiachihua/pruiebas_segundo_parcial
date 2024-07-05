# app.py

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Lista de pacientes (simulación de una base de datos en memoria)
patients = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register_patient():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    age = int(request.form.get('age'))
    dni = request.form.get('dni')
    patient_number = request.form.get('patient_number')
    insured = True if request.form.get('insured') else False

    # Guardar paciente en la lista (simulación de guardar en base de datos)
    patients.append({
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'dni': dni,
        'patient_number': patient_number,
        'insured': insured
    })

    return jsonify({'message': 'Paciente registrado correctamente'})

@app.route('/patients')
def get_patients():
    return jsonify({'patients': patients})

if __name__ == '__main__':
    app.run(debug=True)
