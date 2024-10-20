from flask import Flask, render_template, request
from routes.todo import todos_bp

app = Flask(__name__)
app.register_blueprint(todos_bp, url_prefix='/todo')
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error : msg not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)


# @app.route('/')

# def info_form():
#     return render_template('index.html')

# @app.route('/submit', methods=['POST'])
# def submit():
    
#     name = request.form['name']
#     email = request.form['email']
#     age = request.form['age']
#     password = request.form['password']
#     return render_template('info.html', name=name, email=email, age=age, password=password)

