# algorithms/sjf.py DOSYASIDIR
# ANA FİKİR CPU’ya hazır olan prosesler arasından Burst time’ı  en kısa olan seçilir
# TEMEL NOKTASI en iyi ortalama bekleme süresini
from typing import List, Tuple, Dict
from utils.parser import Process


def sjf_schedule(processes: List[Process]):
    """
    Shortest Job First (Non-preemptive)

    Returns:
        timeline: List of (start, end, pid)
        events: List of execution log strings
        stats: Dict[pid, dict]
        context_switches: int
    """

    time = 0
    completed = set()
    timeline: List[Tuple[int, int, str]] = []
    events: List[str] = []
    stats: Dict[str, Dict] = {}
    context_switches = 0

    n = len(processes)

    while len(completed) < n:
        # Ready queue: arrived & not completed
        ready = [
            p for p in processes
            if p.arrival <= time and p.pid not in completed
        ]

        # CPU idle if nothing is ready
        if not ready:
            next_arrival = min(
                p.arrival for p in processes if p.pid not in completed
            )
            timeline.append((time, next_arrival, "IDLE"))
            events.append(f"t={time}: CPU idle")
            time = next_arrival
            continue

        # Select shortest job (deterministic)
        ready.sort(key=lambda p: (p.burst, p.arrival, p.pid))
        p = ready[0]

        # Context switch (ignore first actual run)
        if timeline and timeline[-1][2] != "IDLE":
            context_switches += 1

        start_time = time
        events.append(f"t={time}: {p.pid} starts running")

        time += p.burst
        end_time = time

        timeline.append((start_time, end_time, p.pid))
        events.append(f"t={end_time}: {p.pid} completes")

        stats[p.pid] = {
            "arrival": p.arrival,
            "burst": p.burst,
            "start": start_time,
            "completion": end_time
        }

        completed.add(p.pid)

    return timeline, events, stats, context_switches
