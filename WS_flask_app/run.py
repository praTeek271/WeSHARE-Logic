from flask import Flask
from config import setup,ErrorHndle
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the WeSHARE API!"


# run flak server
if __name__ == '__main__':
    configure_env=Thread(target=setup)
    configure_env.start()
    print("\n","Starting Flask Server".center(50,"-"),"\n")
    app.run()
