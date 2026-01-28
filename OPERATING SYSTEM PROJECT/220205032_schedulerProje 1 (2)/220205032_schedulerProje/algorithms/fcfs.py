#First Come First Served Scheduling Algorithm Implementation
#FCFS = “Kim önce geldiyse, o önce çalışır” mantığıyla çalışır 
#Sadece arrival time’a bakılır
# Gerçek hayattan örnek vermemiz gerekirse banka kuyruğu gibi

from typing import List, Dict, Tuple
from utils.parser import Process


def fcfs_schedule(processes: List[Process]):
    """
    First Come First Served scheduling (non-preemptive)

    Returns:
        timeline: List of (start_time, end_time, pid)
        events: List of log strings
        stats: Dict[pid, dict]
        context_switches: int
    """

    time = 0
    timeline: List[Tuple[int, int, str]] = []
    events: List[str] = []
    context_switches = 0

    stats: Dict[str, Dict] = {}

    # Sort by arrival time, then PID (deterministic)
    ready = sorted(processes, key=lambda p: (p.arrival, p.pid))

    for p in ready:
        # CPU idle until process arrives
        if time < p.arrival:
            timeline.append((time, p.arrival, "IDLE"))
            events.append(f"t={time}: CPU idle")
            time = p.arrival

        # Context switch (except first run)
        if timeline and timeline[-1][2] != "IDLE":
            context_switches += 1

        # Process starts
        start_time = time
        events.append(f"t={time}: {p.pid} starts running")

        # Run process
        time += p.burst
        end_time = time

        timeline.append((start_time, end_time, p.pid))
        events.append(f"t={end_time}: {p.pid} completes")

        # Save stats
        stats[p.pid] = {
            "arrival": p.arrival,
            "burst": p.burst,
            "start": start_time,
            "completion": end_time
        }

    return timeline, events, stats, context_switches
