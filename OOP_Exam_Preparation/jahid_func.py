def xoxo(heights):
    new={}
    for x,y in heights.items():
        sum=0
        avrg=0.0
        for i in range(len(y)):
            temp=float(y[i])
            # print(temp)
            sum=sum+temp
        # sum=float(sum)
        avrg=sum/len(y)
        # print(avrg)
        new[x]=[avrg]
        
    print(new)

heights={
    'child': [30,40,45,35,30],
    'teenege': [50,60,55,65,60],
    'adult': [85,90,92,88,82],
}
# print(heights)
xoxo(heights)
