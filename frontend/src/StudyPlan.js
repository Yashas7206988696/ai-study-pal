import { useState } from "react";

function StudyPlan() {
  const [subjects, setSubjects] = useState("");
  const [hours, setHours] = useState("");
  const [interests, setInterests] = useState({});
  const [marks, setMarks] = useState({});
  const [plan, setPlan] = useState([]);
  const [chart, setChart] = useState(null);

  const handleInterestChange = (subject, value) => {
    setInterests({ ...interests, [subject]: Number(value) });
  };

  const handleMarksChange = (subject, value) => {
    setMarks({ ...marks, [subject]: value ? Number(value) : null });
  };

  const generatePlan = async () => {
    const subjList = subjects.split(",").map(s => s.trim());
    const res = await fetch("http://localhost:5000/api/studyplan", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ subjects: subjList, hours, interests, marks }),
    });
    const data = await res.json();
    setPlan(data.plan);
    setChart(data.chart);
  };

  const downloadCSV = async () => {
    const subjList = subjects.split(",").map(s => s.trim());
    const res = await fetch("http://localhost:5000/api/download_plan", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ subjects: subjList, hours, interests, marks }),
    });
    const blob = await res.blob();
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "study_plan.csv";
    a.click();
    a.remove();
  };

  return (
    <div style={{ marginTop: "20px" }}>
      <h2>📅 Personalized Study Plan</h2>
      <input value={subjects} onChange={e => setSubjects(e.target.value)} placeholder="Subjects (comma separated)" />
      <input value={hours} onChange={e => setHours(e.target.value)} placeholder="Total hours" type="number" />

      <h3>⚙️ Interest & Marks</h3>
      {subjects.split(",").map((s, i) =>
        s.trim() ? (
          <div key={i}>
            <b>{s.trim()}</b><br/>
            Interest (1-5): <input type="number" min="1" max="5" onChange={e => handleInterestChange(s.trim(), e.target.value)} />
            Marks (0-100, blank=skip): <input type="number" min="0" max="100" onChange={e => handleMarksChange(s.trim(), e.target.value)} />
          </div>
        ) : null
      )}

      <button onClick={generatePlan}>Generate Plan</button>
      <button onClick={downloadCSV}>⬇️ Download CSV</button>

      <ul>{plan.map((p, i) => <li key={i}>{p}</li>)}</ul>

      {chart && <img src={`data:image/png;base64,${chart}`} alt="Study Plan Chart" />}
    </div>
  );
}

export default StudyPlan;
