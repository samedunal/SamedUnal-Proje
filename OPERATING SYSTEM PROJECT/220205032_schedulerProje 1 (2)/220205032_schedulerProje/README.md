  1) Name = Fevzi Samed ÜNAL 
Student ID= 220205032 
Section:3

2) Python Version: Python 3.11.9
Dependencies:
- matplotlib

3) How to run the simulator (sample commands)

- 3.1 FCFS
python scheduler.py --input processes.txt --algo FCFS


- 3.2 SJF
python scheduler.py --input processes.txt --algo SJF


- 3.3 SRTF
python scheduler.py --input processes.txt --algo SRTF


- 3.4 Run Round Robin (quantum required)
python scheduler.py --input processes.txt --algo RR --quantum 4


- 3.5 PRIO_NP
python scheduler.py --input processes.txt --algo PRIO_NP


- 3.6 PRIO_P
python scheduler.py --input processes.txt --algo PRIO_P


- Run all algorithms (Comparison + Graphs)
python scheduler.py --input processes.txt --algo ALL --quantum 4


4) Brief description of each algorithm implementation

- 4.1 FCFS – First Come First Served
Non-preemptive
Processes are executed in order of arrival
Simple but can cause long waiting times

- 4.2 SJF – Shortest Job First
Non-preemptive
Chooses the process with the shortest burst time
Reduces average waiting time compared to FCFS

- 4.3 SRTF – Shortest Remaining Time First
Preemptive version of SJF
A running process can be preempted if a shorter job arrives
Produces very low average waiting and turnaround times

- 4.4 RR – Round Robin
Preemptive
Each process gets a fixed time quantum
Fair scheduling, but higher context switch overhead

- 4.5 PRIO_NP – Priority Scheduling (Non-Preemptive)
Process with highest priority runs until completion
Can cause starvation for low-priority processes

- 4.6 PRIO_P – Priority Scheduling (Preemptive)
Higher priority processes can preempt running ones
Improves response time for high-priority tasks


5) Short discussion of:
 - 5.1 Which algorithm performed best (and why)

Best Performing Algorithm is SRTF (Shortest Remaining Time First) performed best in terms of:
Lowest average waiting time
Lowest average turnaround time
This is expected because SRTF always prioritizes the process with the least remaining execution time.

- 5.2 Any surprising behaviours you observed

Round Robin had the highest waiting time due to frequent context switches.
Priority Scheduling can lead to starvation of low-priority processes.
FCFS, although simple, performs poorly when long jobs arrive early.

6) Terminal outputs (execution logs, Gantt charts, statistics tables) are stored in the screenshots/ directory.

Generated graphs are stored in the graphs/ directory:
avg_waiting.png
avg_turnaround.png






