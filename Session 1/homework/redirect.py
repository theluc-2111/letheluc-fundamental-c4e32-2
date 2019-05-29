from flask import Flask, redirect
app = Flask(__name__)


@app.route('/school')
def index():
    return redirect('http://techkids.vn ')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 