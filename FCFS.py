times=[]
n=int(input("Enter Number of processes : "))
print("Enter arrival time and burst time and pid(int) of each process seperated by , ")
for i in range(n):
    times.append(eval(input()))        


times.sort()


arrival=[0,2,4,6,8]
burst=[3,6,4,5,2]
pid=[1,2,3,4,5]
for  t in times:
    arrival.append(t[0])
    burst.append(t[1])
    pid.append(t[2])
starting=[arrival[0]]
ending=[arrival[0]+burst[0]]
waiting=[(ending[0]-arrival[0])-burst[0]]
tat=[ending[0]-arrival[0]]
sumtat=tat[0]
sumwat=waiting[0]
for i in range(1,len(arrival)):
    starting.append(starting[i-1]+burst[i-1])
    starting[i]=max(starting[i],arrival[i]) #IF CPU IS IDLE
    ending.append(starting[i]+burst[i])
    waiting.append((ending[i]-arrival[i])-burst[i])
    waiting[i]=max(0,waiting[i])  #IF CPU IS IDLE
    tat.append(ending[i]-arrival[i])
    sumtat+=tat[i]
    sumwat+=waiting[i]
print("Process Arrival Burst Starting Ending Waiting TurnAround")
for p,a,b,s,e,w,t in zip(pid,arrival,burst,starting,ending,waiting,tat):
    print("P{:02d} \t {:02d} \t {:02d} \t {:02d} \t {:02d} \t {:02d} \t {:02d}".format(p,a,b,s,e,w,t))
print("\nAvrage TAT:",sumtat/len(tat))
print("Avrage Waiting Time:",sumwat/len(tat))
#Gant Chart
print("Gant Chart : [[Starting Time|--Pid--|Ending Time]]")
for p,s,e in zip(pid,starting,ending):
    print ("[[{:2d}|--P{}--|{:2d}]]".format(s,p,e),end=" -> ")
print("End")