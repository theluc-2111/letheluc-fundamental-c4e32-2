from flask import Flask, render_template
app = Flask(__name__)


# @app.route('/say-hi/<gender>/<name>')
# def say_hi_minh(gender,name):
#     if gender == 'nam':
#         return 'hi anh '+ name
#     else:
#         return 'hi chị ' + name
# @app.route('/say-hi')
# def index():
#     return 'hi'

# @app.route('/tong/<a>/<b>')
# def tong(a,b):
#     return str(int(a) + int(b))
# @app.route('/')
# def index():
#     return """
#     <html>
#     <h1>C4E</h1>
#     <a href='google.com'>google.com</a>
#     <br />
#     <br />
#     <img width='300' heigh='300' src='https://i-giaitri.vnecdn.net/2019/05/26/107110851-2ebf6989-9a26-480c-b-3871-2635-1558857673.jpg'>"""
@app.route('/')
def index():
    poem = {'title': 'Tĩnh dạ tứ',
            'body': 'Nội dung bài thơ',
            'author': 'Lý Bạch'}
   
    poems = []
    poems.append(poem)
    poems.append({'title': 'Thuý Kiều',
                  'body': 'Nội dung bài thơ',
                  'author': 'Nguyễn Du'})
    return render_template('index.html', poems =poems)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
