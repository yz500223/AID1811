def binary(value,key,left,right):
    #递归推出条件
    if left>right:
        return -1
    #获取中间元素下标志
    middle=(left+right)//2
    #对比中间元素值与查找值
    #如果两者相同
    if value[middle]==key:
        return middle
    #如果小于中间值
    elif value[middle]>key:
        return binary(value,key,left,middle-1)
    #如果大于中间值
    else:
        return binary(value,key,middle+1,right)

if __name__=="__main__":
    value=[1,2,3,4,5,6,7,8,9,10,11,12,13]
    key=9
    res=binary(value,key,0,len(value)-1)
    if res==-1:
        print('查找失败')
    else:
        print('查找成功，返回下标识：',res)
    

