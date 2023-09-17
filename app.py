from flask import Flask, render_template, request
from gpt import generate_slides_from_script

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/slideshow', methods=['POST'])
def slideshow():
    script = request.form["data"]
    title_slide, slides = generate_slides_from_script("Script2Slides", script)
    return render_template("slideshow.html", title_slide=title_slide, slideshow=slides)