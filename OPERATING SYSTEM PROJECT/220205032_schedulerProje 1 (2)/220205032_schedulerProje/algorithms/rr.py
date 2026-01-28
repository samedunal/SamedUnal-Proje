# algorithms/rr.py DOSYASIDIR
# TİME=0 DAN BAŞLAYARAK HER BİR ZAMAN BİRİMİNDE GELEN İŞLEMLERİ KONTROL EDER İŞLEYİYİŞİN ANA AMACI BUDUR 
#Kuyruğun başındaki proses çalıştırılır ,min(quantum, remaining time) kadar çalışır.
from typing import List, Tuple, Dict
from collections import deque
from utils.parser import Process


def rr_schedule(processes: List[Process], quantum: int):
    """
    Round Robin Scheduling (Preemptive)

    Returns:
        timeline: List of (start, end, pid)
        events: List of execution log strings
        stats: Dict[pid, dict]
        context_switches: int
    """

    time = 0
    n = len(processes)

    remaining = {p.pid: p.burst for p in processes}
    stats: Dict[str, Dict] = {}
    timeline: List[Tuple[int, int, str]] = []
    events: List[str] = []

    context_switches = 0
    ready_queue = deque()

    # Map arrivals
    arrivals = {}
    for p in processes:
        arrivals.setdefault(p.arrival, []).append(p)

    arrived = set()
    completed = set()
    current_pid = None

    while len(completed) < n:
        # Handle arrivals at current time
        if time in arrivals:
            for p in arrivals[time]:
                ready_queue.append(p)
                arrived.add(p.pid)
                events.append(f"t={time}: {p.pid} arrives")

        # If CPU idle, fetch next
        if current_pid is None:
            if ready_queue:
                p = ready_queue.popleft()
                current_pid = p.pid
                start_time = time

                if current_pid not in stats:
                    stats[current_pid] = {
                        "arrival": p.arrival,
                        "burst": p.burst,
                        "start": time
                    }
                events.append(f"t={time}: {current_pid} starts running")
            else:
                time += 1
                continue

        # Execute for min(quantum, remaining)
        exec_time = min(quantum, remaining[current_pid])
        run_start = time
        run_end = time + exec_time

        # During execution, handle arrivals
        for t in range(time + 1, run_end + 1):
            if t in arrivals:
                for p in arrivals[t]:
                    ready_queue.append(p)
                    arrived.add(p.pid)
                    events.append(f"t={t}: {p.pid} arrives")

        # Advance time
        time = run_end
        remaining[current_pid] -= exec_time
        timeline.append((run_start, run_end, current_pid))

        # Completion
        if remaining[current_pid] == 0:
            events.append(f"t={time}: {current_pid} completes")
            stats[current_pid]["completion"] = time
            completed.add(current_pid)
            current_pid = None
        else:
            # Quantum expired → preempt
            events.append(f"t={time}: quantum expired for {current_pid}")
            ready_queue.append(
                next(p for p in processes if p.pid == current_pid)
            )
            current_pid = None
            context_switches += 1

    return timeline, events, stats, context_switches
