def XoXo(netflix_dic):

    plan_prices = {'Basic': 9.99, 'Standard': 15.99, 'Premium': 19.99}
       
    for user_id, user_info in netflix_dic.items():
        name = user_info['name']
        plan = user_info['plan']
        # print(name) #// siri
        # print(plan) #basic
        payment_amount = plan_prices.get(plan) 
        # print(payment_amount) #Taka aslo eikhane
        if payment_amount is not None:  
            netflix_dic[user_id]['payment'] = payment_amount  #pyment e duklo 
            print(f"Uyee Uyee,{name}! Your payment for the {plan} plan is ${payment_amount} per month.")
        else:
            print("Get lost...")
    
    # print(netflix_dic) #done!
    return netflix_dic


netflix_dic = {
    1: {'name': 'Siri', 'plan': 'Basic'},
    2: {'name': 'Alexa', 'plan': 'Standard'},
    3: {'name': 'Xabbir', 'plan': 'Premium'}
}

netflix_dic = XoXo(netflix_dic)
