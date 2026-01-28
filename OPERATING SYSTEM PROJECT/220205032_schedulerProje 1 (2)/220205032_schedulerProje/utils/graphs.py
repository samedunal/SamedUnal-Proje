# utils/graphs.py DOSYASIDIR
#TEMEL AMACI Algoritmaların performansını görsel olarak karşılaştırmaktır.
# üretilen grafikler şunlardır:
# 1) Average Waiting Time vs Algorithm
# 2) Average Turnaround Time vs Algorithm

import os
import matplotlib.pyplot as plt


def plot_graphs(comparison: dict):
    """
    Generates and saves:
    1) Average Waiting Time vs Algorithm
    2) Average Turnaround Time vs Algorithm
    """

    # graphs/ klasörü yoksa oluştur
    os.makedirs("graphs", exist_ok=True)

    # Algoritma isimleri ve değerler
    algorithms = list(comparison.keys())
    avg_wait = [comparison[a]["waiting"] for a in algorithms]
    avg_turn = [comparison[a]["turnaround"] for a in algorithms]

    # ==================================================
    # Graph 1: Average Waiting Time vs Algorithm
    # ==================================================
    plt.figure()
    plt.bar(algorithms, avg_wait)
    plt.xlabel("Algorithm")
    plt.ylabel("Average Waiting Time")
    plt.title("Average Waiting Time vs Algorithm")
    plt.tight_layout()
    plt.savefig("graphs/avg_waiting.png")
    plt.close()

    # ==================================================
     #Graph 2: Average Turnaround Time vs Algorithm
    # ==================================================
    plt.figure()
    plt.bar(algorithms, avg_turn)
    plt.xlabel("Algorithm")
    plt.ylabel("Average Turnaround Time")
    plt.title("Average Turnaround Time vs Algorithm")
    plt.tight_layout()
    plt.savefig("graphs/avg_turnaround.png")
    plt.close()
