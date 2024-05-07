import time

a=[]
n=int(input('enter the length:'))
for s in range(1,n+1):
    n1=int(input('enter the number:'))
    a.append(n1)
start=time.time()
for i in range(0,n-1):
    for j in range(0,n-1):
        if a[j]<a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)
end=time.time()
print('the time is taken this program is:',end-start)

 
