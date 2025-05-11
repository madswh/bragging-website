from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/resume')
def resume():
    return render_template('templates/static/images/Whitney_Miranda_resume.pdf')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)