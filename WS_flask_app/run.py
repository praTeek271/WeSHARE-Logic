from flask import Flask
from config import setup,ErrorHndle

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    
    setup()
    app.run(debug=True)
