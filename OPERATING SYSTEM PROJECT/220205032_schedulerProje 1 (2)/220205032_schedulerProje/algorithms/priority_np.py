#priority_np.py DOSYASIDIR
#Bir proses başladı mı bitene kadar CPU’dan alınmaz,Arrival time yine önemlidir,
#Sadece CPU boştayken seçim yapılır
#Aynı anda birden fazla proses hazırsa:
# priority’si en küçük olan seçilir VE Preemptive Priority DEN EN BÜYÜK FARKI İŞLEM KESİLMEZ 
#HERHANGİ BİR ÖNCELİK YOKTUR İŞLEMLER ARASINDA. İŞLEM BAŞLADAĞINDA BİTENE KADAR ARALIKSIZ ÇALIŞIR


def prio_np_schedule(processes):
    """
    Non-preemptive Priority Scheduling
    Lower priority value = higher priority
    """

    time = 0
    completed = 0
    n = len(processes)

    timeline = []
    events = []
    stats = {}
    context_switches = 0

# Initialize dynamic fields for each process
    for p in processes:
        p.remaining = p.burst
        p.start_time = None

    # Sort processes by arrival time (deterministic order)
    processes = sorted(processes, key=lambda p: p.arrival)

    # Ready queue
    ready = []

    last_pid = None

    while completed < n:
       # Add newly arrived processes to ready queue
        for p in processes:
            if p.arrival <= time and p not in ready and p.remaining > 0:
                ready.append(p)
      # Filter processes that are not finished  işlemi kesmemk için 
        available = [p for p in ready if p.remaining > 0]

        if available:
            # Select process with highest priority (lowest value) EN ÖNEMLİ KISIM BUDUR ÇÜNKÜ
            #ANA MANTIK EN KÜÇÜK PRIORİTEYİ SEÇMEK ÜZERİNDİR
            current = min(available, key=lambda p: p.priority)

            if last_pid is not None and last_pid != current.pid:
                context_switches += 1
# Process starts execution VE BAŞLAMA ZAMANI ATAMA KISMI
            start = time
            if current.start_time is None:
                current.start_time = time

            events.append(f"t={time}: {current.pid} starts running")
# Process starts execution 
# DİĞER ÖNEMLİ KISIM İŞLEM BİTENE KADAR ARALIKSIZ ÇALIŞTIR 
#ÖNCELİKLE BURADA KESME YOK ÖNCELİKSİZ ŞEKİLDE ÇALIŞTIRIYOR 
            time += current.remaining
            current.remaining = 0
            completed += 1

            events.append(f"t={time}: {current.pid} completes")
            timeline.append((start, time, current.pid))

            stats[current.pid] = {
                "arrival": current.arrival,
                "burst": current.burst,
                "start": current.start_time,
                "completion": time
            }

            last_pid = current.pid
        else:
            # CPU idle if no process is ready
            time += 1

    return timeline, events, stats, context_switches
