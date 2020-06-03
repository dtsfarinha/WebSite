from app import app
from flask import render_template,request,flash
from app import AutFinito, tur

@app.route('/')
@app.route('/index') 
def index(): 
    return render_template("index.html")

@app.route('/regex', methods=["POST","GET"])
def regex():
    if request.method == "POST":
        password = request.form["password"]
        email = request.form["email"]
        ma = AutFinito.mail(email)
        pa = AutFinito.password(password)
        if (ma == pa and pa == "1"):
            flash("GOOD DATA :)")
        else:
            flash("Bad Data")
        return render_template("regex.html" )
    return render_template("regex.html")

@app.route('/AutFinit', methods=["POST","GET"])
def AutFinit():
    if request.method == "POST":
        seq = request.form["sequencia"]
        AutFinito.automato(seq)
        return render_template("AutFinit.html" ) 
    return render_template("AutFinit.html")

@app.route('/AutPilha', methods=["POST","GET"])
def AutPilha():
    if request.method == "POST":
        sequ = request.form["sequen"]
        AutFinito.automata(sequ)
        return render_template("AutPilha.html" ) 
    return render_template("AutPilha.html")

@app.route('/gol') 
def gol(): 
    return render_template("gol.html")

@app.route('/turing', methods=["POST","GET"])
def turing():
    if request.method == "POST":
        seq = request.form["sequencia"]
        AutFinito.automato(seq)
        return render_template("turing.html" ) 
    return render_template("turing.html")

@app.route('/about') 
def about(): 
    return render_template("about.html")