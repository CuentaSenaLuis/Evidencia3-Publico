from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')#Es carpeta raiz

def index():
    data = {
        'Titulos': 'Home'
    }
    return render_template('index.html', data=data)

@app.route('/Cuenta/Login')
def Login():
    data={
        'Titulos': 'Inicio Sesion'
    }
    return render_template('Login.html', data=data)

@app.route('/Cuenta/Registro')
def Register():
    data={
        'Titulos': 'Registro' 
    }
    return render_template('Registro.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
    