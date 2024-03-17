netflix_dic={
    1:{'name':'Siri','plan' :'Basic'},
    2:{'name':'Alexa','plan' :'Standard'},
    3:{'name':'Xabbir','plan' :'Premium'}
}

def calculate_payment(netflix_dic):
  
    plan_prices = {'Basic': 9.99, 'Standard': 15.99, 'Premium': 19.99}

    for user_id, user_info in netflix_dic.items():
        # print(user_id)
        # print(user_info)
        plan = user_info['plan']
        payment_amount = plan_prices.get(plan)
        if payment_amount is not None:
            user_info[plan] = payment_amount

    print(netflix_dic)
    
# Call the function to calculate payments
calculate_payment(netflix_dic)
