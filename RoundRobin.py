times=[tuple([0,3,1]),tuple([2,6,2]),tuple([4,4,3])]#new
n=int(input("Enter Number of processes : "))
print("Enter arrival time and burst time and pid(int) of each process seperated by , ")
burst=13
bt=2
arrival=[0,2,4]
for i in range(n):
    times.append(eval(input()))
    arrival.append(times[1])
    burst+=times[i][1]        
print(burst)
waiting=[]
for i in range(burst):
    if i in arrival:
        indx = arrival.index(i)
        waiting.append(times[indx])
    if i % bt ==0 :
       c = waiting.pop(0)
       print(c)
       if (c[1]-2>0):
        waiting.append(tuple([c[0] , c[1]-2 , c[2]])) 
print(waiting)