from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = ''
    if request.method == 'POST':
        if 'digit' in request.form:
            result = request.form['display'] + request.form['digit']
        elif 'operator' in request.form:
            result = request.form['display'] + request.form['operator']
        elif 'clear' in request.form:
            result = ''
        elif 'calculate' in request.form:
            try:
                result = str(eval(request.form['display']))
            except:
                result = "錯誤"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)