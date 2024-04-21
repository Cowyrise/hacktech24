from flask import Flask, render_template, request
from probability_generator import calculate_probability

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    mother_disorders = request.form.getlist('mother_disorders[]')
    father_disorders = request.form.getlist('father_disorders[]')
    
    # Calculate the probability of the child having each disorder
    prediction_result = calculate_probability(mother_disorders, father_disorders)
    
    return render_template('result.html', prediction_result=prediction_result)

if __name__ == '__main__':
    app.run(debug=True)
