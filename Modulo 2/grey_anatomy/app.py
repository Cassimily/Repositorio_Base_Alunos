from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/personagens")
def personagens():
    return render_template("personagens.html")

@app.route("/temporadas")
def temporadas():
    return render_template("temporadas.html")


if __name__ == "__main__":
    app.run(debug=True)