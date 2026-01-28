# utils/comparison.py DOSYASIDIR
#PROJE YÖNERGE DOSYAMIZDAKİ 6.4 DEKİ TABLOYU GÖSTERMEK İÇİN BU DOSYAYI OLUŞTURDUM
#AMACI Tüm algoritmalar çalıştırıldıktan sonra ortalama metrikleri tek bir tabloda gösteir .
#BU TABLO DA ŞU METRİKLER VARDIR;
#Average Turnaround Time, 
# Average Waiting Time, 
# Average Response Time, 
# Context Switches Count.

def print_comparison_table(comparison: dict):
    """
    Prints Algorithm Comparison Summary table (Section 6.4)

    Expected comparison format:
    {
        "FCFS": {
            "turnaround": float,
            "waiting": float,
            "response": float,
            "context": int
        },
        ...
    }
    """

    print("\n=== Algorithm Comparison Summary ===\n")

    header = (
        f"{'Algorithm':<10}"
        f"{'Avg Turn':>12}"
        f"{'Avg Wait':>12}"
        f"{'Avg Resp':>12}"
        f"{'Ctx Switch':>14}"
    )
    print(header)
    print("-" * len(header))

    order = ["FCFS", "SJF", "SRTF", "RR", "PRIO_NP", "PRIO_P"]

    for algo in order:
        if algo not in comparison:
            continue

        r = comparison[algo]

        print(
            f"{algo:<10}"
            f"{r['turnaround']:>12.2f}"
            f"{r['waiting']:>12.2f}"
            f"{r['response']:>12.2f}"
            f"{r['context']:>14}"
        )
