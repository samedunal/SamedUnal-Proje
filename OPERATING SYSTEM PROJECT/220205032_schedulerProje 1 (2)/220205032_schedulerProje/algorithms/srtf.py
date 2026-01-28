# algorithms/srtf.py DOSYASIDIR
# EN TEMEL KISMI CPU HER AN Hazır prosesler arasında kalan süresi en az olan HANGİSİ İSE ONA BAKAR VE SEÇER
# Eğer daha kısa kalan süreli bir proses gelirse Mevcut proses kesilir (preemption)
from typing import List, Tuple, Dict
from utils.parser import Process


def srtf_schedule(processes: List[Process]):
    """
    Shortest Remaining Time First (Preemptive)

    Returns:
        timeline: List of (start, end, pid)
        events: List of execution log strings
        stats: Dict[pid, dict]
        context_switches: int
    """

    # Initialize
    time = 0
    n = len(processes)

    remaining = {p.pid: p.burst for p in processes}
    arrived = set()
    completed = set()

    timeline: List[Tuple[int, int, str]] = []
    events: List[str] = []
    stats: Dict[str, Dict] = {}

    context_switches = 0
    current_pid = None
    segment_start = None

    # Pre-calc arrival times
    arrivals = {}
    for p in processes:
        arrivals.setdefault(p.arrival, []).append(p)

    while len(completed) < n:
        # Register arrivals at current time
        if time in arrivals:
            for p in arrivals[time]:
                arrived.add(p.pid)
                events.append(f"t={time}: {p.pid} arrives")

        # Ready processes (arrived but not completed)
        ready = [
            p for p in processes
            if p.pid in arrived and p.pid not in completed
        ]

        if not ready:
            # CPU idle
            if current_pid is not None:
                timeline.append((segment_start, time, current_pid))
                current_pid = None

            time += 1
            continue

        # Select process with shortest remaining time
        ready.sort(
            key=lambda p: (remaining[p.pid], p.arrival, p.pid)
        )
        selected = ready[0]

        # Context switch / preemption
        if current_pid != selected.pid:
            if current_pid is not None:
                timeline.append((segment_start, time, current_pid))
                events.append(
                    f"t={time}: {selected.pid} preempts {current_pid}"
                )
                context_switches += 1

            current_pid = selected.pid
            segment_start = time

            # First response time
            if selected.pid not in stats:
                stats[selected.pid] = {
                    "arrival": selected.arrival,
                    "burst": selected.burst,
                    "start": time
                }
                events.append(f"t={time}: {selected.pid} starts running")

        # Execute 1 time unit
        remaining[current_pid] -= 1
        time += 1

        # Completion
        if remaining[current_pid] == 0:
            timeline.append((segment_start, time, current_pid))
            events.append(f"t={time}: {current_pid} completes")

            stats[current_pid]["completion"] = time
            completed.add(current_pid)

            current_pid = None
            segment_start = None

    return timeline, events, stats, context_switches
