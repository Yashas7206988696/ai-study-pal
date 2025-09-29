from flask import Flask, request, jsonify, send_file, send_from_directory
from flask_cors import CORS
import io, csv
from ai_planner import make_study_plan, plot_pie_chart
from ai_quiz_model import generate_quiz
from ai_summarizer import summarize_text
from ai_feedback import motivational_feedback
from ai_tips import extract_study_tips

import os

# If a production build of the frontend exists, serve its static files from Flask's static folder
FRONTEND_BUILD_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'frontend_interface', 'build'))
STATIC_DIR = os.path.join(FRONTEND_BUILD_DIR, 'static')

# Create the Flask app with the static_folder pointed at the frontend build's static files
app = Flask(__name__, static_folder=STATIC_DIR, static_url_path='/static')
CORS(app)

@app.route('/<path:path>')
def serve_frontend(path):
    # Try serving direct static files from the build folder (index and assets)
    if os.path.exists(FRONTEND_BUILD_DIR):
        file_path = os.path.join(FRONTEND_BUILD_DIR, path)
        if os.path.exists(file_path):
            # If the path points into the static subtree, let Flask static handler serve it
            if path.startswith('static/'):
                return app.send_static_file(path[len('static/'):])
            return send_from_directory(FRONTEND_BUILD_DIR, path)
    return jsonify({'error': 'Not found'}), 404

@app.route('/')
def serve_index():
    if os.path.exists(FRONTEND_BUILD_DIR):
        return send_from_directory(FRONTEND_BUILD_DIR, 'index.html')
    return "Welcome to AI Study Pal backend"

# ---------------- Study Plan ----------------
@app.route("/api/studyplan", methods=["POST"])
def study_plan():
    data = request.get_json()
    subjects = data["subjects"]
    hours = int(data["hours"])
    interests = data.get("interests", {})
    marks = data.get("marks", {})

    plan, allocation = make_study_plan(subjects, hours, interests, marks)
    chart = plot_pie_chart(allocation)
    return jsonify({"plan": plan, "allocation": allocation, "chart": chart})

# ---------------- Download Study Plan CSV ----------------
@app.route("/api/download_plan", methods=["POST"])
def download_plan():
    data = request.get_json()
    subjects = data["subjects"]
    hours = int(data["hours"])
    interests = data.get("interests", {})
    marks = data.get("marks", {})

    plan, allocation = make_study_plan(subjects, hours, interests, marks)

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Hour", "Task"])
    for i, task in enumerate(plan, start=1):
        writer.writerow([i, task])
    output.seek(0)

    return send_file(
        io.BytesIO(output.getvalue().encode("utf-8")),
        mimetype="text/csv",
        as_attachment=True,
        download_name="study_plan.csv"
    )


# ...existing API routes...

# ---------------- Quiz ----------------
@app.route("/api/quiz", methods=["POST"])
def quiz():
    data = request.get_json()
    subject = data["subject"]
    level = int(data.get("level", 1))
    quiz = generate_quiz(subject, level)
    return jsonify({"quiz": quiz})

# ---------------- Summarizer ----------------
@app.route("/api/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    text = data["text"]
    summary = summarize_text(text)
    return jsonify({"summary": summary})

# ---------------- Feedback ----------------
@app.route("/api/feedback", methods=["POST"])
def feedback():
    data = request.get_json()
    subject = data["subject"]
    msg = motivational_feedback(subject)
    return jsonify({"feedback": msg})

# ---------------- Tips ----------------
@app.route("/api/tips", methods=["POST"])
def tips():
    data = request.get_json()
    text = data["text"]
    tips = extract_study_tips(text)
    return jsonify({"tips": tips})

if __name__ == "__main__":
    app.run(debug=True)
