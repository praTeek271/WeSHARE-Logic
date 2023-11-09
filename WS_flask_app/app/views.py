from flask import Flask,render_template,request
from app.fire_base_handling import fire_base_handling as fbhndl

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
        user=request.form['username']
        password=request.form['password']
        try:
            user_key=fbhndl.create_user(user,password)
        except Exception as e:
            print(e)
            return render_template('index.html',user_key=f"ERROR due to {e}")
        return render_template('index.html',user_key=user_key)

    return render_template('index.html')


# if __name__=="__main__":
#     fbhndl=fbhndl().create_user("test","test123456")
