from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def index(username):
    user = {'luc': {'age': 24, 'address': 'Hà Nội', 'hobby': 'Liên quân Mobile'},
            'duy': {'age': 22, 'address': 'Hà Nội', 'hobby': 'Liên Minh Huyền Thoại'},
            'ahoa': {'age': 30, 'address': 'Thái Bình', 'hobby': 'Cạo đầu'}}
    return render_template('user.html', user=user, username=username)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
