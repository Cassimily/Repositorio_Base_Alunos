from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

## Continue o código aqui.

@app.route("/soma")
def  soma():
    v1 = float(request.args.get("valor1"))
    v2 = float(request.args.get("valor2"))
    resultado = v1+v2

    return {"Resultado" : resultado}


@app.route("/subtrair")
def  subtrair():
    v1 = float(request.args.get("valor1"))
    v2 = float(request.args.get("valor2"))
    resultado = v1-v2

    return {"Resultado" : resultado}


@app.route("/multiplicar")
def multiplicar():
    v1 = float(request.args.get("valor1"))
    v2 = float(request.args.get("valor2"))
    resultado = v1 * v2

    return {"Resultado": resultado}


@app.route("/dividir")
def dividir():
    v1 = float(request.args.get("valor1"))
    v2 = float(request.args.get("valor2"))
    resultado = v1 / v2

    return {"Resultado": resultado}

@app.route("/divisao")
def divisao():
    v1 = float(request.args.get("valor1"))
    v2 = float(request.args.get("valor2"))

    if v2 == 0:
        return {"Erro": "Não é possível dividir por zero"}

    resultado = v1 / v2

    return {"Resultado": resultado}



if __name__ == "__main__":
    app.run(debug=True)
