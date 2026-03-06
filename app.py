from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "PRUEBA SUPERADA XDDD"

if __name__ == "__main__":
    app.run()
