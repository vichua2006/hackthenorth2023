from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/slideshow', methods=['POST'])
def slideshow():
    script = request.form["data"]
    print(script)
    slides = [
        {
            "title": "Hi!",
            "points": [
                "point 1",
                "point 2",
            ]
        }
    ]
    return render_template("slideshow.html", slideshow=slides)

app.run(debug=True)