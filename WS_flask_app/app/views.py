from flask import Flask,render_template

app = Flask(__name__,template_folder='templates')

@app.route('/')
def home():
    return "Welcome to the WeSHARE API!"

@app.route('/<string:endpoint>')
def endpoint(endpoint):
    # return f"No page on \t\' http://localhost/{endpoint} \'"
     return render_template('404.html',endpoint=endpoint)
