from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    body = {'weight':61,'height':169}
    BMI = body['weight']/((body['height']/100)**2)
    return render_template('idex_BMI.html', BMI = BMI)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)