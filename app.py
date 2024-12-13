from flask import Flask, render_template, request
import pandas as pd
import joblib

# Cargar el modelo entrenado
model = joblib.load('model.pkl')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Verificar si el archivo se puede leer
    try:
        df = pd.read_csv('static/ubigeo.csv')  # Ruta correcta a la carpeta 'static'
        print(df.head())  # Verifica que el CSV se haya cargado correctamente
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")

    if request.method == 'POST':
        # Obtener los datos del formulario
        data = {
            'UBIGEO_POSTULANTE': [int(request.form['ubigeo_postulante'])],
            'EDAD': [int(request.form['edad'])],
            'PAIS': [int(request.form['pais'])],
            'UBIGEO_EMPRESA': [int(request.form['ubigeo_empresa'])],
            'EDAD_MINIMA_PARA_EL_TRABAJO': [int(request.form['edad_minima'])],
            'EDAD_MAXIMA_PARA_EL_TRABAJO': [int(request.form['edad_maxima'])],
            'NUMERO_VACANTES': [int(request.form['vacantes'])],
            'NUMERO_POSTULANTES': [int(request.form['postulantes'])],
            'SEXO_VARON': [int(request.form['sexo_varon'])],
            'SEXO_MUJER': [int(request.form['sexo_mujer'])],
            'SEXO_SOLICITUD_VARON': [int(request.form['sexo_solicitud_varon'])],
            'SEXO_SOLICITUD_MUJER': [int(request.form['sexo_solicitud_mujer'])],
            'SEXO_SOLICITUD_NO_REQUIERE': [int(request.form['sexo_solicitud_no_requiere'])],
        }
        # Convertir los datos en un DataFrame
        new_data = pd.DataFrame(data)

        # Realizar la predicción
        prediction = model.predict(new_data)
        probability = model.predict_proba(new_data)

        # Mostrar el resultado
        return render_template('index.html', prediction=prediction[0], probability=probability[0])

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
