from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask("plank")
db = SQLAlchemy(app)


class Model(db.Model):
	__tablename__ = "model"
	id = db.Column(db.Integer, primary_key=True)
	model_name = db.Column(db.String)
	model_hash = db.Column(db.String)
	model_score = db.Column(db.String)
	model_algo = db.Column(db.String)


@app.route("/upload", methods=["POST"])
def upload_model():
   if request.method == "POST":
      
      file = request.files["filename"]
      file.save("static/{}".format(file.filename))
      
      with open("static/{}".format(file.filename)) as f:
         content = f.readlines()

      payload = {"status": "200 OK", "content":  content}
      return jsonify(payload)


@app.route("/")
def index_page():
   return render_template("index.html")


if __name__ == "__main__":
   app.run(port=8888)


