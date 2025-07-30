# interpreter.py

def interpret_history(history):
    H_values = history["H"]
    A_values = history["A"]
    E_values = history["E"]

    final_H = H_values[-1]
    final_A = A_values[-1]
    final_E = E_values[-1]

    interpretation = []

    # تحلیل بر اساس مقدار هویت
    if final_H < 0.3:
        interpretation.append("- Severe identity erosion.")
    elif final_H < 0.6:
        interpretation.append("- Moderate struggle with personal identity.")
    else:
        interpretation.append("- Strong sense of identity retained.")

    # تحلیل بر اساس پذیرش اجتماعی
    if final_A > 0.7:
        interpretation.append("- High need for social approval.")
    elif final_A > 0.4:
        interpretation.append("- Moderate concern for social acceptance.")
    else:
        interpretation.append("- Low concern for external validation.")

    # تحلیل بر اساس پوچی
    if final_E > 0.7:
        interpretation.append("- Rising existential emptiness may lead to distress.")
    elif final_E > 0.4:
        interpretation.append("- Signs of emotional fatigue.")
    else:
        interpretation.append("- Emotional state relatively stable.")

    return "\n".join(interpretation)
