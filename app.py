from flask import Flask, render_template, request, session, redirect, url_for
from calculate_probabilities import calculate_probability
from email_results import email_results

app = Flask(__name__)
app.secret_key = 'hacktech24'  # Set a secret key for session management

@app.route('/', methods=['GET','POST'])
def index():
    if(request.method == 'POST'):
        email_recipient = request.form.get('email-recipient')
        # Send an email_recipient
        print(email_results(email_recipient, session['prediction_result']))
        return redirect(url_for('predict'))  # Redirect to page with the results again 
    else:
        print('Session: ' + str(session['prediction_result']))
        return render_template('index.html')
    # get the email_results
    # abstract away the password
    # reload onto the same page so the results are still visibile
    # email validation

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        mother_disorders = request.form.getlist('mother_disorders[]')
        print(mother_disorders)
        father_disorders = request.form.getlist('father_disorders[]')
        # Calculate the probability of the child having each disorder
        prediction_result = calculate_probability(mother_disorders, father_disorders)
        session['prediction_result'] = prediction_result  # Store prediction_result in session

    return render_template('result.html', prediction_result=session['prediction_result'])

if __name__ == '__main__':
    app.run(debug=True)
