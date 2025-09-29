# AI Study Pal

Simple Flask backend + React frontend for study planning, quizzes, summarization and tips.

## Setup (backend)

1. Create a virtual environment and activate it (Windows PowerShell):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the backend:

```powershell
python backend\app.py
```

The backend will start on http://127.0.0.1:5000 by default.

## Setup (frontend)

From `frontend_interface` run:

```powershell
cd frontend_interface; npm install; npm start
```

This will open the React dev server on http://localhost:3000.

## Notes
- Matplotlib is configured to use the 'Agg' backend so the server can render charts without a display.
- If you add or change dependencies, update `requirements.txt` accordingly.
