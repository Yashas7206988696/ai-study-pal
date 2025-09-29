import pandas as pd
import ast
import json
import csv

df = pd.read_csv(
    'backend/questions.csv',
    engine='python',
    quotechar='"',
    escapechar='\\'
)

def generate_quiz(subject, level=1, num_questions=5):
    df_sub = df[(df["subject"].str.lower() == subject.lower()) & (df["difficulty"] == level)]

    if df_sub.empty:
        df_sub = df[df["subject"].str.lower() == subject.lower()]

    if df_sub.empty:
        return [{"error": f"No questions found for subject: {subject}"}]

    quiz_data = df_sub.sample(min(num_questions, len(df_sub)))[
        ["question", "options", "answer", "difficulty"]
    ].to_dict(orient="records")

    for item in quiz_data:
        try:
            item["options"] = ast.literal_eval(item["options"])  # parse string to Python list
            item["options"] = json.dumps(item["options"])        # convert Python list to JSON string
        except (ValueError, SyntaxError):
            item["options"] = "[]"  # send empty if error

    return quiz_data
