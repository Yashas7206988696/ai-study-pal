<<<<<<< HEAD
import io
import base64
import matplotlib
# Use a non-interactive backend to avoid GUI/display issues when running on servers
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def make_study_plan(subjects, hours, interests, marks):
    total_weight = 0
    weights = {}

    for subj in subjects:
        mark = marks.get(subj, None)
        interest = interests.get(subj, 3)
        weight = (100 - mark) / 2 if mark is not None else 0
        weight += (6 - interest) * 2
        weights[subj] = max(1, weight)
        total_weight += weights[subj]

    allocation = {s: round((w / total_weight) * hours) for s, w in weights.items()}

    plan = []
    hour_count = 1
    for subj, hrs in allocation.items():
        for h in range(hrs):
            plan.append(f"Hour {hour_count}: Study {subj} (focus topic {h+1})")
            hour_count += 1

    return plan, allocation

def plot_pie_chart(allocation):
    fig, ax = plt.subplots()
    ax.pie(allocation.values(), labels=allocation.keys(), autopct="%1.1f%%")
    ax.set_title("Study Plan Distribution")
    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    chart_base64 = base64.b64encode(img.read()).decode("utf-8")
    plt.close(fig)
    return chart_base64
=======
import io
import base64
import matplotlib
# Use a non-interactive backend to avoid GUI/display issues when running on servers
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def make_study_plan(subjects, hours, interests, marks):
    total_weight = 0
    weights = {}

    for subj in subjects:
        mark = marks.get(subj, None)
        interest = interests.get(subj, 3)
        weight = (100 - mark) / 2 if mark is not None else 0
        weight += (6 - interest) * 2
        weights[subj] = max(1, weight)
        total_weight += weights[subj]

    allocation = {s: round((w / total_weight) * hours) for s, w in weights.items()}

    plan = []
    hour_count = 1
    for subj, hrs in allocation.items():
        for h in range(hrs):
            plan.append(f"Hour {hour_count}: Study {subj} (focus topic {h+1})")
            hour_count += 1

    return plan, allocation

def plot_pie_chart(allocation):
    fig, ax = plt.subplots()
    ax.pie(allocation.values(), labels=allocation.keys(), autopct="%1.1f%%")
    ax.set_title("Study Plan Distribution")
    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    chart_base64 = base64.b64encode(img.read()).decode("utf-8")
    plt.close(fig)
    return chart_base64
>>>>>>> e60b692163850de42bdbad1168022c06d8707106
