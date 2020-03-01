from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "A civilization that leaves so many of it's citizens unsatisfied and drives"
    return "them to revolt, neither has nor deserves the prospect of a lasting existance."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
