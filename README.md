# SchedulingAlgorithms
Implementation OS Scheduling algorithms that I studied during my 4th semester

Sample FCFS Output:
```
Process Arrival Burst Starting Ending Waiting TurnAround
P01      00      03      00      03      00      03
P02      02      06      03      09      01      07
P03      04      04      09      13      05      09
P04      06      05      13      18      07      12
P05      08      02      18      20      10      12
P09      00      02      20      22      20      22
P07      01      05      22      27      21      26
P08      02      06      27      33      25      31

Avrage TAT: 15.25
Avrage Waiting Time: 11.125
Gant Chart : [[Starting Time|--Pid--|Ending Time]]
[[ 0|--P1--| 3]] -> [[ 3|--P2--| 9]] -> [[ 9|--P3--|13]] -> [[13|--P4--|18]] -> [[18|--P5--|20]] -> [[20|--P9--|22]] -> [[22|--P7--|27]] -> [[27|--P8--|33]] -> End
```

Sample Round Robin
```
Enter Number of processes : 3
Enter arrival time and burst time and pid(int) of each process seperated by , 
0,5,1
2,3,2
3,1,3
Enter Preemption Time2
Gant Chart : [[Starting Time|--Pid--|Ending Time]]
[[ 0|--P1--| 2]] -> [[ 2|--P2--| 4]] -> [[ 4|--P1--| 6]] -> [[ 6|--P3--| 7]] -> [[ 7|--P2--| 8]] -> [[ 8|--P1--| 9]] -> END

PID     Arrival Burst   Starting        End     TAT     Waiting
P1            0       5       0       9       9       4
P2            2       3       2       8       6       3
P3            3       1       6       7       4       3
```
