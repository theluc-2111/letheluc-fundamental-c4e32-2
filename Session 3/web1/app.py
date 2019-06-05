from flask import Flask, render_template, request, redirect, url_for
from mongo import get_all,insert_food,get_food_by_id,update_food_by_id
app = Flask(__name__)
 

@app.route('/edit_food/<food_id>',methods = ['POST'])
def put_food(food_id):
    dish_name = request.form.get('name')
    dish_price = int(request.form.get('price'))
    update_food_by_id(food_id,dish_name,dish_price)
    return redirect(url_for('index'))
 
@app.route('/edit_food/<food_id>')
def func_name(food_id):
    print(food_id)
    dish=get_food_by_id(food_id) 
    return render_template('edit_food.html',food = dish)


@app.route('/', methods=['POST'])
def post_dish():
    dish_name = request.form.get('name')
    dish_price = int(request.form.get('price'))
    insert_food(dish_name,dish_price) 
    return redirect(url_for('index'))


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", data=get_all() )


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
