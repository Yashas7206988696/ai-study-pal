import { useState } from "react";

function Summarizer() {
  const [text, setText] = useState("");
  const [summary, setSummary] = useState("");

  const summarize = async () => {
    const res = await fetch("http://localhost:5000/api/summarize", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });
    const data = await res.json();
    setSummary(data.summary);
  };

  return (
    <div style={{ marginTop: "20px" }}>
      <h2>📖 Summarizer</h2>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Enter text to summarize"
        rows={4}
        cols={50}
      />
      <br />
      <button onClick={summarize}>Summarize</button>
      {summary && (
        <p>
          <b>Summary:</b> {summary}
        </p>
      )}
    </div>
  );
}

export default Summarizer;
