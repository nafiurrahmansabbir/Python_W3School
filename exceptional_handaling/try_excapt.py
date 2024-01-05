try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

# ..........###----main Fabda---------###------------#

try:
  print("Hello")
except:
  print("Something went wrong") #try e na dukle excenption e dukbe
else:
  print("Nothing went wrong") # try e dukle else eu dukbe
# agin:
try:
  print(x)
except:
  print("Something went wrong") #try e na dukle excenption e dukbe
else:
  print("Nothing went wrong") # try e dukle else eu dukbe

#   finaly
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished") #always dukbe

# raise
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")
x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")