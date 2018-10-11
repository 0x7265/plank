from flask import Flask, request, jsonify

app = Flask("plank")

@app.route("/upload", methods=["POST"])
def upload_model():
   if request.method == "POST":
      file = request.files["filename"]
      file.save("static/{}".format(file.filename))
      with open("static/{}".format(file.filename)) as f:
         content = f.readlines()

      payload = {"status": "200 OK", "content":  content}
      return jsonify(payload)


if __name__ == "__main__":
   app.run(port=8888)


