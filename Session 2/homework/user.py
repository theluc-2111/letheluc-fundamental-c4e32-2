from flask import Flask, request, render_template,redirect,url_for
app = Flask(__name__)

list_pass = {'khanh':'1','luc':'1111111','ahoa':'121212','h':'123123'}

@app.route('/')
def login():
  return render_template('login.html')

@app.route('/',methods= ['POST'])
def result():
  username = request.form.get('username')
  password = request.form.get('password')
  if username in list_pass and password == list_pass[username]:
    return 'Login Successfull'
  else:
    return 'Login Failed!'
  return redirect(url_for('login'))

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 