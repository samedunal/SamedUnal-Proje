# utils/parser.py DOSYASIDIR
#processes.txt) okur ve Process nesneleri listesi döner.Tüm algoritmaların kullandığı ortak veri kaynağıdır
#DAHA AÇIK VE TEMEL ŞEKİLDE FCFS, SJF, SRTF, RR, Priority hepsi bu dosyadan gelen Process listesiyle çalışır
from dataclasses import dataclass
from typing import List


@dataclass
class Process:
    pid: str
    arrival: int
    burst: int
    priority: int


def parse_processes(path: str) -> List[Process]:
    """
    Reads processes from a text file.
    Rules:
    - Lines starting with '#' are ignored
    - Fields are whitespace-separated:
      pid arrival_time burst_time priority
    """
    processes: List[Process] = []

    with open(path, "r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.strip()

            # Ignore comments and empty lines
            if not line or line.startswith("#"):
                continue

            parts = line.split()
            if len(parts) != 4:
                raise ValueError(f"Invalid line format: {line}")

            pid = parts[0]
            arrival = int(parts[1])
            burst = int(parts[2])
            priority = int(parts[3])

            processes.append(
                Process(pid=pid, arrival=arrival, burst=burst, priority=priority)
            )

    # Deterministic order (important for grading)
    processes.sort(key=lambda p: (p.arrival, p.pid))
    return processes
