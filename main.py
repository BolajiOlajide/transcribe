import os

from flask import Flask, render_template, request, jsonify

from transcribe import audio_transcribe


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/transcribe", methods=["POST"])
def transcribe():
    audio_file = request.files.get('file')
    result = audio_transcribe(audio_file)
    template = render_template("result.html", result=result)
    return jsonify({'template': template})

if __name__ == "__main__":
    port = os.getenv('PORT', 5000)
    app.run(debug=True, port=port)
