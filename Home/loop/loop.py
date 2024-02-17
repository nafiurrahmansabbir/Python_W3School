n=int(input("Enter number: "))

# for x in range(2, 30, 3):
#   print(x)
# for x in range(1,6,2):
#   print(x)

if(n>=100) and (n<=200):
    for x in range(1,n+1):
        if(x%2==0):
            print(x*x*x)
        else:
            print(x*x)
    
else:
    print("Input not in range!")


# for x in range(1,n+1):
#         if(x%2==0):
#             print(x*x*x)
#         else:
#             print(x*x)
