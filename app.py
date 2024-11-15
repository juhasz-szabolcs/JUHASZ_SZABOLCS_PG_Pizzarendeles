from flask import Flask, render_template, request

app = Flask(__name__)

# Lista a rendelések tárolásához
orders = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pizza-order', methods=['GET', 'POST'])
def pizza_order():
    if request.method == 'POST':
        _name = request.form['name']
        _phone = request.form['phone']
        _size = request.form['size']
        _toppings = request.form.getlist('toppings')
        _quantity = request.form['quantity']
        _delivery_time = request.form['delivery_time']
        _comments = request.form['comments']

                # Az új rendelés hozzáadása a listához
        order = {
            'name': _name,
            'phone': _phone,
            'size': _size,
            'toppings': _toppings,
            'quantity': _quantity,
            'delivery_time': _delivery_time,
            'comments': _comments
        }
        orders.append(order)

        return render_template('order_summary.html', orders=orders)
    return render_template('pizza_order.html')


@app.route('/order-summary')
def order_summary():
    return render_template('order_summary.html', orders=orders)


if __name__ == '__main__':
    app.run(debug=True)

