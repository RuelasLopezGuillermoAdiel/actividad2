from flask import Flask , render_template, request , redirect ,url_for ,flash

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta_super_segura'

@app.route("/base")
def inicio():
    return render_template("base.html")

@app.route("/index")
def principal():
    return render_template("index.html")

@app.route("/verificar", methods=["POST"])
def verificar():
    r1 = request.form.get("respuesta1")
    r2 = request.form.get("respuesta2")
    r3 = request.form.get("respuesta3")

    if r1:
        if r1.strip().lower() == "flask":
            flash("Tarea 1: ✅ Correcto!", "success")
        else:
            flash("Tarea 1: ❌ Incorrecto", "error")

    if r2:
        if "card" in r2.lower():
            flash("Tarea 2: ✅ Correcto!", "success")
        else:
            flash("Tarea 2: ❌ Incorrecto", "error")

    if r3:
        if "number" in r3.lower() or "número" in r3.lower():
            flash("Tarea 3: ✅ Correcto!", "success")
        else:
            flash("Tarea 3: ❌ Incorrecto", "error")

    return redirect(url_for("principal"))



if __name__ == "__main__":
    app.run(debug=True)
