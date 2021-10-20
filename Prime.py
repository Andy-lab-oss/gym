from flask import Flask, render_template, request
app = Flask(__name__)





@app.route('/templates/index.html')
def inicio():
    return render_template("index.html")

@app.route('/templates/Formulario.html')
def Mayor():
   return render_template('Formulario.html')

@app.route('/templates/Historia.html')
def History():
   return render_template('Historia.html')

@app.route('/templates/bitcoin.html')
def Bitcoin():
   return render_template('bitcoin.html')

@app.route('/templates/link.html')
def Enlace():
   return render_template('link.html')


   
   

if __name__ == '__main__':
   app.run(debug = True)