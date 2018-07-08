from flask import Flask
from flask import render_template

# app = Flask(__name__,template_folder="haha") #可以手动指定模板的存储路径
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/Nonja")
def nonja():
    return render_template("Nonja.html")


@app.route("/piaopiao")
def piaopiao():
    return render_template("piaopiao.html")


if __name__ == "__main__":
    app.run(host="45.32.34.139", port="5055", debug=False)
