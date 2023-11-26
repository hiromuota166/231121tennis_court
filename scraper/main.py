from flask import Flask, render_template
from t_danjyo import danjyo

app = Flask(__name__)

@app.route('/')
def index():
    # t_danjyo.pyのmain()の処理を実行
    # ここに取得したデータを格納

    data = danjyo()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
