from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    info = {'name':'Lực','age':20,'address':'Hà Nội','hobby':'Liên quân Mobile'}
    return render_template('about_me.html',info = info)
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)