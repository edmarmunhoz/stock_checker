import os
from flask import Flask, request, render_template, make_response
from sklearn.externals import joblib
import pandas as pd

app = Flask(__name__, static_url_path='/static')
model = joblib.load('model.pkl')

@app.route('/')
def display_gui():
    return render_template('template.html')

@app.route('/verificar', methods=['POST'])
def verificar():
    abertura = request.form['abertura']
    minimo = request.form['minimo']
    maximo = request.form['maximo']
    volume = request.form['volume']
    score = request.form['score']

    data = {'Abertura': [abertura], 'Minimo': [minimo], 'Maximo': [maximo], 'Volume': [volume], 'Score': [score]}

    novo_teste = pd.DataFrame(data)

    print("Teste")
    print("Abertura: {}".format(abertura))
    print("Minimo: {}".format(minimo))
    print("Maximo: {}".format(maximo))
    print("Volume: {}".format(volume))
    print("Score: {}".format(score))
    print("\n")

    classe = model.predict(novo_teste)
    print("Resultado do teste: {}".format(classe))

    return render_template('template.html', classe=str(classe[0]))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5500))
    app.run(host='0.0.0.0', port=port)