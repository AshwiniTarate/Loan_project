import pickle
import json
import numpy as np



class Bad_loan_prediction():
    def prediction(loan_amnt,term,int_rate,emp_length,home_ownership,annual_inc,purpose,addr_state,dti,delinq_2yrs,revol_util,total_acc,longest_credit_length,verification_status):
        decision_tree=pickle.load(open('artifacts\loan dt model.pickle','rb'))
        file = json.load(open('artifacts\Feature names.json','r'))['data_columns']
        
        mon = term.lower()
        month =file.index(mon)
    
        home_ownership = home_ownership.lower()
        home_own = file.index(home_ownership)
    
        purpose = purpose.lower()
        purp = file.index(purpose)
    
        address_state = addr_state.lower()
        add_st = file.index(address_state)
        
        verification_status=verification_status.lower()
        verify = file.index(verification_status)
        m = np.zeros(len(file))
        
        m[0] = loan_amnt
        m[month] = 1
        m[2] = float(int_rate)
        m[3] = float(emp_length)
        m[home_own] = 1 
        m[4] = float(annual_inc)
        m[purp] = 1
        m[add_st] = 1
        m[5] = float(dti)
        m[6] = delinq_2yrs
        m[7] = revol_util
        m[8] = total_acc
        m[9] = longest_credit_length
        m[verify] = 1
        return decision_tree.predict([m])[0]

if __name__ == "__main__":
    result= Bad_loan_prediction.prediction(1.265720,'60 months',15.27,0.0,'rent',10.308953,'car','GA',1.00,0,9.4,3.174802,26,'verified')
    print('Loan is {}'.format(result))