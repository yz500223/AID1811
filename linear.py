
def linear(value,key):
    for i in range(len(value)):
        if value[i]==key:
            return i
    else:
        #查找失败，返回－１
        return -1
    
if __name__=='__main__':
    value=[3,1,2,5,7,4,6,9,11,13,12,10,8]
    key=6

    res=linear(value,key)
    if res==-1:
        print('查找失败')
    else:
        print('查找成功，返回下标识：',res)