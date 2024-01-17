from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        result = perform_operation(num1, num2, operation)

        return render_template('calculator.html', result=result)

def perform_operation(num1, num2, operation):
    operations = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,
        'divide': lambda x, y: x / y if y != 0 else 'Cannot divide by zero',
    }

    return operations.get(operation, lambda x, y: 'Invalid operation')(num1, num2)


if __name__ == '__main__':
    app.run(debug=True)
