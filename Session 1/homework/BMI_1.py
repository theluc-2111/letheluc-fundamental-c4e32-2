from flask import Flask
app = Flask(__name__)


@app.route('/bmi/<weight>/<height>')
def bmi(weight,height):
    BMI = int(weight)/((int(height)/100)**2)
    if BMI < 16:
        return "BMI: " + str(BMI) +' | Severely underweight'
    elif BMI < 18.5:
        return "BMI: " + str(BMI) +' | Underweight'
    elif BMI < 25:
        return "BMI: " + str(BMI) +' | Normal' 
    elif BMI < 30:
        return "BMI: " + str(BMI) +' | Overweight'
    else:
        return "BMI: " + str(BMI) +' | Obese'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
