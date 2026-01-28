# utils/statistics.py DOSYASIDIR
# Tüm algoritmalar çalıştıktan sonra: Turnaround Time, Waiting Time, Response Time gibi metrikleri hesaplar.
#Ortalama Turnaround Time, Ortalama Waiting Time, Ortalama Response Time gibi metrikleri hesaplar ve yazdırır.
from typing import Dict, Tuple


def compute_statistics(stats: Dict[str, Dict]) -> Tuple[Dict[str, Dict], Dict[str, float]]:
    """
    stats input format:
    {
      pid: {
        "arrival": int,
        "burst": int,
        "start": int,
        "completion": int
      }
    }
    """

    results: Dict[str, Dict] = {}

    total_turnaround = 0
    total_waiting = 0
    total_response = 0
    n = len(stats)
# Compute metrics for each process
    for pid, s in stats.items():
        arrival = s["arrival"]
        burst = s["burst"]
        start = s["start"]
        completion = s["completion"]

        turnaround = completion - arrival
        waiting = turnaround - burst
        response = start - arrival

        results[pid] = {
            "arrival": arrival,
            "burst": burst,
            "completion": completion,
            "turnaround": turnaround,
            "waiting": waiting,
            "response": response
        }

        total_turnaround += turnaround
        total_waiting += waiting
        total_response += response
# Compute averages
    averages = {
        "avg_turnaround": total_turnaround / n if n else 0,
        "avg_waiting": total_waiting / n if n else 0,
        "avg_response": total_response / n if n else 0
    }

    return results, averages


def print_statistics_table(results: Dict[str, Dict], averages: Dict[str, float]):
    print("\n--- Per-Process Statistics ---")
    print("PID  Arr  Burst  Compl  Turn  Wait  Resp")

    for pid in sorted(results.keys()):
        r = results[pid]
        print(
            f"{pid:<4} "
            f"{r['arrival']:<4} "
            f"{r['burst']:<6} "
            f"{r['completion']:<6} "
            f"{r['turnaround']:<5} "
            f"{r['waiting']:<5} "
            f"{r['response']:<5}"
        )

    print("\n--- Averages ---")
    print(f"Average Turnaround Time: {averages['avg_turnaround']:.2f}")
    print(f"Average Waiting Time:    {averages['avg_waiting']:.2f}")
    print(f"Average Response Time:   {averages['avg_response']:.2f}")
