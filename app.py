from flask import Flask, render_template

app = Flask(__name__)

@app.route('/Cuenta/Home')#Es carpeta raiz

def index():
    titulos = ['Home', 'Registro', 'Inicio Sesion']
    data = {
        'Titulos': titulos
    }
    return render_template('index.html', data=data)

@app.route('/Cuenta/Login')
def Login():
    titulos = ['Home', 'Registro', 'Inicio Sesion']
    data={
        'Titulos': titulos
    }
    return render_template('Login.html', data=data)

@app.route('/Cuenta/Registro')
def Register():
    titulos = ['Home', 'Registro', 'Inicio Sesion']
    data={
        'Titulos': titulos
    }
    return render_template('Registro.html', data=data)

if __name__ == '__main__':
    app.run()
    