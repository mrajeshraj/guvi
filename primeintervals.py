a,b =map(int,input().split())
for x in range(a + 1,b):
   if x > 1:
       for i in range(2,x):
           if (x % i) == 0:
               break
       else:
            print(x,end=" ")
