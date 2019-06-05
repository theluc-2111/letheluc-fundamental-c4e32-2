from flask import Flask, render_template, request, redirect, url_for
from mongo import insert_food,get_all
app = Flask(__name__)
# menu = [{'name': 'cơm rang', 'price': '10k'},
#         {'name': 'bún bò', 'price': '20k'},
#         {'name': 'cơm gà', 'price': '30k'}]


@app.route('/', methods=['POST'])
def post_dish():
    dish_name = request.form.get('name')
    dish_price = request.form.get('price')
    # menu.append({'name': dish_name,
    #              'price': dish_price})
    # 
    # return render_template('index.html', menu=menu)
    print(dish_name)
    insert_food(dish_name,dish_price)
    return redirect(url_for('index'))

@app.route('/')
def index():
    # dish_name = request.args.get('name')
    return render_template('index.html', data=get_all())


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
