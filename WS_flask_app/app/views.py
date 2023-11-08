from flask import Flask,render_template
import fire_base_handling as firebHandl

app = Flask(__name__,template_folder='templates',static_folder='static')


#----------------------------------------
@app.route('/<string:endpoint>')
def endpoint(endpoint):
    # return f"No page on \t\' http://localhost/{endpoint} \'"
     return render_template('404.html',endpoint=endpoint)
#----------------------------------------



@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        
    return "Welcome to the WeSHARE API!"
