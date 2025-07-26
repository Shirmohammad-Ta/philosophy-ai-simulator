# simulation.py

def run_simulation(steps=51):
    history = {
        "H": [],
        "A": [],
        "E": [],
    }

    # مقدار اولیه برای H (Identity), A (Acceptance)
    H = 1.0
    A = 0.3
    E = 0.0

    for t in range(steps):
        V = 1 - H  # میزان از خودگذشتگی
        delta_E = A * V  # تاثیر پذیرش بر پوچی
        E += delta_E * 0.05
        H = max(H - A * 0.01, 0)  # کم شدن هویت
        A = min(A + 0.01, 1.0)  # افزایش تلاش برای پذیرفته شدن

        history["H"].append(H)
        history["A"].append(A)
        history["E"].append(E)

    return history
