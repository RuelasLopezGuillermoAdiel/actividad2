from flask import Flask , render_template, request , redirect ,url_for ,flash

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta_super_segura'

@app.route("/")
def inicio():
    return render_template("base.html")

@app.route("/")
def principal():
    return render_template("index.html")
