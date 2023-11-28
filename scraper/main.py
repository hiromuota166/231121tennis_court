from flask import Flask, render_template, url_for
from t_danjyo import danjyo

app = Flask(__name__)

@app.route('/')
def index():
    data = danjyo()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
