from flask import Flask
from config import setup,ErrorHndle
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the WeSHARE API!"

@app.route('/<string:endpoint>')
def endpoint(endpoint):
    return f"No page on \t\' http://localhost/{endpoint} \'"

# run flak server
if __name__ == '__main__':
    configure_env=Thread(target=setup)
    configure_env.start()
    print("\n","Starting Flask Server".center(50,"-"),"\n")
    try:
        app.run(debug=True)
    except KeyboardInterrupt or Exception as e:
        ErrorHndle().handle_and_exit(mesaage="Server Stopped",e=e)
    finally:
        # configure_env.join()
        print("\n","Server Stopped".center(50,"-"),"\n")
