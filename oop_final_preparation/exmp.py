print('start')
d=0
try:
    d=2/0
except:
    print("Exeption")
else:
    d=10
    print("try e dukse ty else e dukse")
finally:
    print("Ami 12 vatari")
    
print(d)
print('End')


x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")
x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")

print("--------------------end============")