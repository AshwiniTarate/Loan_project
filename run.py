from flask import Flask,request,render_template,jsonify
import test
import loan_db
import config

app = Flask(__name__,template_folder='template')

@app.route('/')
def index():
   return render_template('predict_loan.html')

@app.route('/months', methods=['GET'])
def months():
    response = jsonify({'term':test.Bad_loan_prediction.prediction()})
    return response

@app.route('/home', methods=['GET'])
def home_name():
    response = jsonify({'home_ownership':test.Bad_loan_prediction.prediction()})
    return response

@app.route('/addr', methods=['GET'])
def  addr_name():
    response = jsonify({'addr_state': test.Bad_loan_prediction.prediction()})
    return response



@app.route('/purps', methods=['GET'])
def pur_names():
    response = jsonify({'purpose': test.Bad_loan_prediction.prediction()})
    return response

@app.route('/status', methods=['GET'])
def status_names():
    response = jsonify({'verification_status': test.Bad_loan_prediction.prediction()})
    return response



@app.route('/bad_loan', methods=['GET', 'POST'])
def predict_loan():
    if request.method == 'POST':
        loan_amnt = int(request.form['loan_amnt'])
        term = request.form.get('term')
        int_rate = float(request.form['int_rate'])
        emp_length=float(request.form['emp_length'])
        home_ownership=request.form.get('home_ownership')
        annual_inc=float(request.form['annual_inc'])
        purpose=request.form.get('purpose')
        addr_state=request.form.get('addr_state')
        dti=float(request.form['dti'])
        delinq_2yrs=float(request.form['delinq_2yrs'])
        revol_util=float(request.form['revol_util'])
        total_acc =float(request.form['total_acc'])
        longest_credit_length =float(request.form['longest_credit_length'])
        verification_status=request.form.get('verification_status')
        prediction = test.Bad_loan_prediction.prediction(loan_amnt ,term,int_rate,emp_length, home_ownership, annual_inc, purpose, addr_state, dti, delinq_2yrs ,revol_util, total_acc , longest_credit_length, verification_status)
        data=request.form
        loan_db.lon_data(data)
        if prediction==0:
            messsage='Good Customer'
        else:
            messsage='Bad Customer'
        
        # return "The loan is {} that means {}".format(prediction,messsage)

    

    return render_template('predict_loan.html',prediction_text = "The Loan is {}".format(prediction),messsage=messsage)



if __name__ == "__main__":
    print("Starting Python Flask Server For Bad Loan Prediction...")
    app.run(port=config.port)