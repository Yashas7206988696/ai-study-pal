import { useState } from "react";

function Feedback() {
  const [subject, setSubject] = useState("");
  const [feedback, setFeedback] = useState("");

  const getFeedback = async () => {
    const res = await fetch("http://localhost:5000/api/feedback", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ subject }),
    });
    const data = await res.json();
    setFeedback(data.feedback);
  };

  return (
    <div style={{ marginTop: "20px" }}>
      <h2>💬 Motivational Feedback</h2>
      <input
        value={subject}
        onChange={(e) => setSubject(e.target.value)}
        placeholder="Enter subject"
      />
      <button onClick={getFeedback}>Get Feedback</button>
      {feedback && <p>{feedback}</p>}
    </div>
  );
}

export default Feedback;
