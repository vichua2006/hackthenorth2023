from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates", static_folder="statics")

@app.route('/')
@app.route('/index', methods=['POST', 'GET'])
@app.route('/presentation', method=['POST', 'GET'])

def index():
    return render_template('index.html')

def presentation():
    return render_template('presentation.html', script=request.args.get('script'))

if __name__ == "__main__":
    app.run(debug=True)