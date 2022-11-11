



def main():
    list1 = [1,2,3,4,5,6,7,8,9,10]
    list2=[]
    dic={}
    for n in list1:
        list2.append(n*n)
    dic=dict(zip(list1,list2))
    nn = dic.values()
    for i in nn:
        if i==(6*6):
            print(i)

    price = [10020,1000,100,10,10]
    for n in map(lambda x:x-(x*0.2), price):
        print(int(n))

main()