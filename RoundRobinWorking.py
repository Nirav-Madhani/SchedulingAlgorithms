times=[]#[(0,3,1),(2,1,2),(4,4,3)]
total=0
n=int(input("Enter Number of processes : "))
print("Enter arrival time and burst time and pid(int) of each process seperated by , ")
for i in range(n):
    times.append(eval(input()))    
    total+=times[i][1]    
##n=3
times.sort()
processMap=[] # arr Bur Id beg End TAT wait
#print(times)
for t in times:
    processMap.append(list(t)+[-1,-1,-1,-1])
#print(processMap)
T=times[0][0]
active=list(times.pop(0))
waiting=[]
BT=eval(input("Enter Burst Time"))
done=[]
##total = 8 #############Comment this
while T<total:
    #print(active)
    t=T
    T+=min(active[1],BT)    
    
    i=0
    #print(T)
    while (i<len(times)):
        if (times[i][0]<=T):
            waiting.append(times.pop(i))
        else:
            i+=1
    
    active[1]-=min(BT,active[1])
    done.append(tuple(active+[t,T]))#(Arrival,BurstTime Left,ProcessID,Start,Finish)
    #print("Done :",active)
    if (active[1]!=0):
        waiting.append(tuple(active))
    if T==total:
        break
    try:
        active=list(waiting.pop(0))
    except:#When CPU will be IDLE
        T=times[0][0]
        active.append(times.pop(0))
#print(waiting)
print("Gant Chart : [[Starting Time|--Pid--|Ending Time]]")
for d in done:
    print("[[{:2d}|--P{}--|{:2d}]]".format(d[3],d[2],d[4]),end=" -> ")
    for c in processMap:
        if d[2]==c[2] :
            c[4]=d[4] 
            if c[3]==-1:
                c[3] = d[3]
print("END\n")
for x in processMap:
    x[5]=x[4]-x[0]
    x[6]=x[5]-x[1]
#
# print (processMap)
print("PID\tArrival\tBurst\tStarting\tEnd\tTAT\tWaiting")
for k in processMap:
    print("P{:}\t{:7d}\t{:7d}\t{:7d}\t{:7d}\t{:7d}\t{:7d}".format(k[2],k[0],k[1],k[3],k[4],k[5],k[6]))



