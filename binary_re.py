def binary(value,key):
    left=0
    right=len(value)-1
    while left<=right:
        middle=(left+right)//2
        if value[middle]==key:
            return middle
    #如果大于中间值
        elif value[middle]<key:
            left=middle+1
    #如果小于中间值
        else:
            right=middle-1
            
    return -1
if __name__=="__main__":
    value=[1,2,3,4,5,6,7,8,9,10,11,12,13]
    key=9
    res=binary(value,key)
    if res==-1:
        print('查找失败')
    else:
        print('查找成功，返回下标识：',res)
    