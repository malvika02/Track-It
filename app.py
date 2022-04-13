from distutils.log import debug
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLAlchemy_DATABASE_URI'] = "sqlite:///track-it.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#the imported SQLAlchemy 
db = SQLAlchemy(app)

class track(db.model):
    username = db(db.string(50), nullable = False)


@app.route("/")
def hello():
    return render_template("login.html")
    

if __name__ == "__main__":
    app.run(debug = True, port=8400)