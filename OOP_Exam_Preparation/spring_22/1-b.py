def waiver(result,amount):
    if result>=3.50 and result<=4:
        print('20%')
        waiver=(20/100)*amount
    elif result>=3 and result<3.50:
        print("10%")
        waiver=(20/100)*amount
    elif result<3:
        print("5%")
        waiver=(20/100)*amount
        
    return waiver
    

def main():
    result=float(input("Enter your CGPA: "))
    amount=float(input("Enter your amount: "))
    temp=waiver(result,amount)
    print(temp)
    
if __name__=="__main__":
    main()
    