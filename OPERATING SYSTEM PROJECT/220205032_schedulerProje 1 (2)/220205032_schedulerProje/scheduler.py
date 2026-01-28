# scheduler.py
import argparse

from utils.parser import parse_processes
from utils.statistics import compute_statistics, print_statistics_table
from utils.gantt import print_ascii_gantt
from utils.comparison import print_comparison_table
from utils.graphs import plot_graphs

from algorithms.fcfs import fcfs_schedule
from algorithms.sjf import sjf_schedule
from algorithms.srtf import srtf_schedule
from algorithms.rr import rr_schedule
from algorithms.priority_np import prio_np_schedule
from algorithms.priority_p import prio_p_schedule


def run_single(algo_name, processes, quantum=None):
    """Run a single scheduling algorithm and return:
       (timeline, events, stats, context_switches)
    """
    if algo_name == "FCFS":
        return fcfs_schedule(processes)

    if algo_name == "SJF":
        return sjf_schedule(processes)

    if algo_name == "SRTF":
        return srtf_schedule(processes)

    if algo_name == "RR":
        if quantum is None:
            raise ValueError("quantum is required for RR")
        return rr_schedule(processes, quantum)

    if algo_name == "PRIO_NP":
        return prio_np_schedule(processes)

    if algo_name == "PRIO_P":
        return prio_p_schedule(processes)

    raise ValueError(f"Unknown algorithm: {algo_name}")


def main():
    parser = argparse.ArgumentParser(description="CPU Scheduling Simulator")

    parser.add_argument("--input", required=True, help="Path to processes.txt")
    parser.add_argument(
        "--algo",
        required=True,
        choices=["FCFS", "SJF", "SRTF", "RR", "PRIO_NP", "PRIO_P", "ALL"],
        help="Scheduling algorithm",
    )
    parser.add_argument("--quantum", type=int, help="Time quantum (required for RR)")

    args = parser.parse_args()

    # ==================================================
    # ALL MODE → Section 6.4 + 6.5 (TABLE + GRAPHS)
    # ==================================================
    if args.algo == "ALL":
        quantum = args.quantum if args.quantum is not None else 4

        algorithms = ["FCFS", "SJF", "SRTF", "RR", "PRIO_NP", "PRIO_P"]
        comparison = {}

        for name in algorithms:
            # each algorithm must start from clean input
            processes = parse_processes(args.input)

            timeline, events, stats, ctx = run_single(name, processes, quantum)

            _, averages = compute_statistics(stats)

            comparison[name] = {
                "turnaround": averages["avg_turnaround"],
                "waiting": averages["avg_waiting"],
                "response": averages["avg_response"],
                "context": ctx,
            }

        # 6.4 – Comparison Table
        print_comparison_table(comparison)

        # 6.5 – Graphs (saved to graphs/)
        plot_graphs(comparison)

        return

    # ==================================================
    # SINGLE ALGORITHM MODE
    # ==================================================
    processes = parse_processes(args.input)

    if args.algo == "RR" and args.quantum is None:
        parser.error("--quantum is required when --algo RR is selected")

    print(f"Loaded {len(processes)} processes")
    print(f"Selected algorithm: {args.algo}")

    timeline, events, stats, context_switches = run_single(
        args.algo, processes, args.quantum
    )

    # =========================
    # EXECUTION LOG
    # =========================
    print("\n--- Execution Log ---")
    for e in events:
        print(e)

    # =========================
    # GANTT TIMELINE
    # =========================
    print("\n--- Gantt Timeline ---")
    for seg in timeline:
        print(seg)

    # =========================
    # ASCII GANTT CHART
    # =========================
    print_ascii_gantt(timeline)

    # =========================
    # STATISTICS
    # =========================
    results, averages = compute_statistics(stats)
    print_statistics_table(results, averages)

    # =========================
    # CONTEXT SWITCHES
    # =========================
    print("\n--- Context Switches ---")
    print(context_switches)


if __name__ == "__main__":
    main()
