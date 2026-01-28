#ÇALIŞMA MANTIĞI PRIO_NP İLE  EN BÜYÜK FARKI BURDA İŞLEM KESİLEBİLİR.  



def prio_p_schedule(processes):
    """
    Preemptive Priority Scheduling
    Lower priority value = higher priority
    """

    time = 0
    completed = 0
    n = len(processes)

    timeline = []
    events = []
    stats = {}
    context_switches = 0

    current = None
    segment_start = None

    # Reset dynamic fields
    for p in processes:
        p.remaining = p.burst
        p.start_time = None
# Main scheduling loop (runs until all processes end)
    while completed < n:
        # Ready queue
        ready = [
            p for p in processes
            if p.arrival <= time and p.remaining > 0
        ]

        if ready:
            # Pick highest priority process (lowest priority value) ÖNEMLİ KISIM AMAÇ İÇİN
            selected = min(ready, key=lambda p: p.priority)

            # Context switch (PID change)
            # Context switch if selected process changes 
            # PRİORİTY.NP DEN AYIRICI KISIM  BURDA İŞLEM KESİLEBİLİR
            if current != selected:
                if current is not None:
                    timeline.append((segment_start, time, current.pid))
                    context_switches += 1
                    events.append(
                        f"t={time}: {selected.pid} preempts {current.pid}"
                    )

                current = selected
                segment_start = time

                if current.start_time is None:
                    current.start_time = time
                    events.append(
                        f"t={time}: {current.pid} starts running"
                    )

            # Run for 1 time unit
            current.remaining -= 1
            time += 1

            # Completion
            if current.remaining == 0:
                timeline.append((segment_start, time, current.pid))
                completed += 1

                events.append(
                    f"t={time}: {current.pid} completes"
                )

                stats[current.pid] = {
                    "arrival": current.arrival,
                    "burst": current.burst,
                    "start": current.start_time,
                    "completion": time
                }

                # Context switch after completion (if others exist)
                if completed < n:
                    context_switches += 1

                current = None
                segment_start = None
        else:
            # CPU idle
            time += 1

    return timeline, events, stats, context_switches
