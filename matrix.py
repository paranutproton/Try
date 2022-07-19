import numpy as np
arr = np.array([[9,2,3],[4,5,6],[7,8,9]])
print(arr)

def cal_diagonal(arr):
    plus = 0
    minus = 0
    #a=0
    #b=0
    c=len(arr)-1
    #d=0
    for i in range (0,len(arr),1):
        plus += arr[i][i]
        
        minus += arr[c][i]
        
        #a += 1
        #b += 1 
        c -= 1
        #d += 1
    print(plus)
    print(minus)
    ans = plus - minus
    #return print(f"ทะแยงลง: {plus} ทะแยงขึ้น: {minus} ลบได้ {ans}")
    return plus,minus,ans

plus,minus,ans = cal_diagonal(arr)
print(f"ทะแยงลง: {plus} ทะแยงขึ้น: {minus} ลบได้ {ans}")
