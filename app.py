from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')

def info_form():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    password = request.form['password']
    return render_template('info.html', name=name, email=email, age=age, password=password)

if __name__ == '__main__':
    app.run(debug=True)

