from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pizza-order', methods=['GET', 'POST'])
def pizza_order():
    return render_template('pizza_order.html')


if __name__ == '__main__':
    app.run(debug=True)
