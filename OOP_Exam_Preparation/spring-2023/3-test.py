def cal(keys, values):
    my_dic = {}

    for i in range(len(keys)):
        my_dic[keys[i]] = values[i]
    
    return my_dic

def main():
    K = [1001, 1002, 1003, 1004, 1005]
    V = ["USA", "Canada", "China", "Japan", "UK"]
    temp={}
    temp = cal(K, V)
    print(temp)
    print(temp.keys)

if __name__ == "__main__":
    main()
