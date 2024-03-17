
# spring 2023-01-B

def Number(list):
    
    # Create a copy of the original list
    newNumber=list.copy()
    
    # Reverse the list
    newNumber.reverse()
    
     # Sort the original list
    NumberSort=sorted(list)
    
    return newNumber,NumberSort

list = [181, 178, 187, 182, 192, 189, 202, 201]

reverse,sortedNumber=Number(list)
print('orginal ',list)
print('reverse ',reverse)
print('sorted ',sortedNumber)


# spring 2023-03-B
def listToDist(k,v):
    keyvalue=zip(k,v)
    dictconvert=dict(keyvalue)
    return dictconvert
k=[1001,1002,1003,1004]
v=["USA","CANADA","CHINA","DOTTOPARA","UK"]
result=listToDist(k,v)
print(result)

# spring 2023-01-A

list = [181, 178, 187, 182, 192, 189, 202, 201]
print(list)


#spring-2022-1-A

value = [1, 2, 3, 4, 5, 6, 7, 8, 9]
value2 = [1, 2, 3]
for item in value:
    if item == 5:
        continue
    print('break')
    for item2 in value2:
        print(item, item2)

#spring-2022-1-B
stu=float(input('enter your result :'))
if stu>4.00:
    print("something  is wrong .")
elif stu>=3.5:
    print("20 % waiver") 
elif 3.00<= stu <3.50:
    print("10% waiver")
elif stu<3.00:
    print("5% waiver")


#spring-2022-1-C
list=[]
for num in  range(1,101):
    if num%2!=0:
        list.append(num)
print(list)


# spring 2023-01-B

def Number(list):
    
    # Create a copy of the original list
    newNumber=list.copy()
    
    # Reverse the list
    newNumber.reverse()
    
     # Sort the original list
    NumberSort=sorted(list)
    
    return newNumber,NumberSort

list = [181, 178, 187, 182, 192, 189, 202, 201]

reverse,sortedNumber=Number(list)
print('orginal ',list)
print('reverse ',reverse)
print('sorted ',sortedNumber)


# spring 2023-03-B
def listToDist(k,v):
    keyvalue=zip(k,v)
    dictconvert=dict(keyvalue)
    return dictconvert
k=[1001,1002,1003,1004]
v=["USA","CANADA","CHINA","DOTTOPARA","UK"]
result=listToDist(k,v)
print(result)


# spring 2023-01-A

list = [181, 178, 187, 182, 192, 189, 202, 201]
print(list)


#spring-2022-1-A

value = [1, 2, 3, 4, 5, 6, 7, 8, 9]
value2 = [1, 2, 3]
for item in value:
    if item == 5:
        continue
    print('break')
    for item2 in value2:
        print(item, item2)


#spring-2022-1-B
stu=float(input('enter your result :'))
if stu>4.00:
    print("something  is wrong .")
elif stu>=3.5:
    print("20 % waiver") 
elif 3.00<= stu <3.50:
    print("10% waiver")
elif stu<3.00:
    print("5% waiver")


#spring-2022-1-C
list=[]
for num in  range(1,101):
    if num%2!=0:
        list.append(num)
print(list)


#spring-2022-1-B
list1=[1,2,3,5]
list2=[2,4,5,3]

common_elements = set(list1) and set(list2)
if common_elements:
    print("Common elements:", list(common_elements))
else:
    print("No common elements")

# spring 2023-01-B

def Number(list):
    
    # Create a copy of the original list
    newNumber=list.copy()
    
    # Reverse the list
    newNumber.reverse()
    
     # Sort the original list
    NumberSort=sorted(list)
    
    return newNumber,NumberSort

list = [181, 178, 187, 182, 192, 189, 202, 201]

reverse,sortedNumber=Number(list)
print('orginal ',list)
print('reverse ',reverse)
print('sorted ',sortedNumber)

# spring 2023-03-B
def listToDist(k,v):
    keyvalue=zip(k,v)
    dictconvert=dict(keyvalue)
    return dictconvert
k=[1001,1002,1003,1004]
v=["USA","CANADA","CHINA","DOTTOPARA","UK"]
result=listToDist(k,v)
print(result)


# spring 2023-01-A

list = [181, 178, 187, 182, 192, 189, 202, 201]
print(list)

#spring-2022-1-A

value = [1, 2, 3, 4, 5, 6, 7, 8, 9]
value2 = [1, 2, 3]
for item in value:
    if item == 5:
        continue
    print('break')
    for item2 in value2:
        print(item, item2)


#spring-2022-1-B
stu=float(input('enter your result :'))
if stu>4.00:
    print("something  is wrong .")
elif stu>=3.5:
    print("20 % waiver") 
elif 3.00<= stu <3.50:
    print("10% waiver")
elif stu<3.00:
    print("5% waiver")


#spring-2022-1-C
list=[]
for num in  range(1,101):
    if num%2!=0:
        list.append(num)
print(list)


#spring-2022-1-B
list1=[1,2,3,5]
list2=[2,4,5,3]

common_elements = set(list1) and set(list2)
if common_elements:
    print("Common elements:", list(common_elements))
else:
    print("No common elements")


#spring-2022-02-c
userinput=input("enter the number ").split()


inputToiNT=[int(x) for x in userinput]

if len(inputToiNT) < 3:
    print("not possible ")
else:
    newlist=inputToiNT[1:-1]
    print("new list ",newlist)
    