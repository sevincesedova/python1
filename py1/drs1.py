#task1
"""
a=int(input("1-ci ededi daxil edin: "))
b=int(input("2-ci ededi daxil edin: "))
c=int(input("3-cu ededi daxil edin: "))
d=int(input("4-cu ededi daxil edin: "))
e=int(input("5-ci ededi daxil edin: "))
list=[a,b,c,d,e]
print(list)
list.sort()
print(list)

"""
#task2
"""
cumle=str(input("istediyiniz cumleni daxill edin: "))
print("".join((sorted(cumle))))

"""
#task3
""""
n=13
count=0
while True :
    eded=int(input("ededi tap: "))
    count+=1
    if eded==n:
        print(f"Doğrudur. {count} addimda tapdiniz")
        break
        
"""
#task4
for i in range(2,100):
            x = False
            for j in range(2,i):
                if i % j == 0:
                    x=True
                    break
            if x == False:
                print (i)