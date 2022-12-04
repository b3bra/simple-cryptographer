from flask import render_template, redirect, url_for
from app.forms import EncodeForm, DecodeForm
from app import app
import base64

@app.route("/")
def index():
    return render_template("index.html", title = "Хз главная")

@app.route("/encode", methods = ["GET", "POST"])
def encode():
    form = EncodeForm()
    if form.validate_on_submit():
        result = "".join([base64.b85encode(ord(i).to_bytes(2, "big")).decode() for i in form.data.data])
        return render_template("encode.html", title = "Encode", form = form, result = result)
    return render_template("encode.html", title = "Encode", form = form)

@app.route("/decode", methods = ["GET", "POST"])
def decode():
    form = DecodeForm()
    if form.validate_on_submit():
        step = 3
        result = []
        for i in range(int(len(form.data.data) / 3)):
            chunk = form.data.data[step - 3:step]
            result.append(chr(int.from_bytes(base64.b85decode(chunk), "big")))
            step += 3
        return render_template("decode.html", title = "Encode", form = form, result = "".join(result))
    return render_template("decode.html", title = "Encode", form = form)
