from flask import Flask,request,jsonify
import os
import joblib
# import sklearn
# print(sklearn.__version__)   #1.0.2

app = Flask(__name__)

BASE_DIR = os.getcwd()
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
FILENAME = os.path.join(STATIC_ROOT,'finalized_model.sav')


@app.route('/api/loan_approval',methods=['GET','POST'])
def loan_approval():
    if(request.method=='POST'):
        
        Gender = request.form['Gender']
        Married = request.form['Married']
        Education = request.form['Education']
        Self_Employed = request.form['Self_Employed']
        Credit_History = request.form['Credit_History']

        g = 1 if Gender == 'Male' else 0
        m = 1 if Married == 'Yes' else 0
        e = 1 if Education == 'Not Graduate' else 0
        s = 1 if Self_Employed == 'Yes' else 0
        c = float(Credit_History)

        # print(Gender)
        # print(g)
        # print(Married)
        # print(m)
        # print(Education)
        # print(e)
        # print(Self_Employed)
        # print(s)
        # print(Credit_History)
        # print(c)

        model = joblib.load(FILENAME)

        Loan_Status = model.predict([[g,m,e,s,c]])
        

        # return str(Loan_Status)
        return jsonify({"Loan_Status":int(Loan_Status[0])})

    if(request.method=='GET'):
        print('get')
    return 'Not a valid request'

if __name__ == '__main__':
    app.run(debug=True,port=9090,host='0.0.0.0')