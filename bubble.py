 
def bubble(value):
    for i in range(len(value)-1):
        for j in range(len(value)-i-1):
            if value[j]>value[j+1]:
                value[j],value[j+1]=value[j+1],value[j]
    
    print('遍历次数',i+1)
if __name__=='__main__':
    value=[120,145,165,187,134,166,157,175,155,169]
    print('排序前的：',value)
    bubble(value)
    print('排序后的：',value)
