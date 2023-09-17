from flask import Flask, render_template, request
from gpt import generate_slides_from_script

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/slideshow', methods=['POST'])
def slideshow():
    script = request.form["data"]
    points, links = generate_slides_from_script(script)
    slides = zip(points, links)
    
    return render_template("slideshow.html", slideshow=slides)

# @app.route('/loading', )

app.run(debug=True)