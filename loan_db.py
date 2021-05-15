from pymongo import MongoClient
import config


db_name = config.HPP_DATABASE
myclient = MongoClient(config.MONGODB_URL)
db = myclient[db_name]

collection_prediction = db['prediction_details']




# def bad_loan_details(loan_amnt,term,int_rate,emp_length,home_ownership,annual_inc,purpose,addr_state,dti,delinq_2yrs,revol_util,total_acc,longest_credit_length,verification_status,prediction):
#     loan_details = {'loan_amnt': loan_amnt,'term':term,'int_rate':int_rate ,'emp_length':emp_length,'home_ownership':home_ownership,'annual_inc':annual_inc,'purpose':purpose,'addr_state':addr_state,'dti':dti,'delinq_2yrs':delinq_2yrs,'revol_util':revol_util,'total_acc':total_acc,'longest_credit_length':longest_credit_length,'verification_status':verification_status, ' prediction':prediction}
            
#     collection_prediction.insert_one(loan_details)

#     return 'saved successfully'


def lon_data(pred_loan_dict):
    user_dict={}
    user_dict['loan_amnt']=pred_loan_dict['loan_amnt']
    user_dict['term']=pred_loan_dict['term']
    user_dict['int_rate']=pred_loan_dict['int_rate']
    user_dict['emp_length']=pred_loan_dict['emp_length']
    user_dict['home_ownership']=pred_loan_dict['home_ownership']
    user_dict['annual_inc']=pred_loan_dict['annual_inc']
    user_dict['purpose']=pred_loan_dict['purpose']
    user_dict['addr_state']=pred_loan_dict['addr_state']
    user_dict['dti']=pred_loan_dict['dti']
    user_dict['delinq_2yrs']=pred_loan_dict['delinq_2yrs']
    user_dict['revol_util']=pred_loan_dict['revol_util']
    user_dict['total_acc']=pred_loan_dict['total_acc']
    user_dict['longest_credit_length']=pred_loan_dict['longest_credit_length']
    user_dict['verification_status']=pred_loan_dict['verification_status']

    collection_prediction.insert_one(user_dict)
    return 'Saved Successfully'
    

