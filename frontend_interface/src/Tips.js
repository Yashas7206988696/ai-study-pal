import { useState } from "react";

function Tips() {
  const [text, setText] = useState("");
  const [tips, setTips] = useState([]);

  const getTips = async () => {
    const res = await fetch("http://localhost:5000/api/tips", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });
    const data = await res.json();
    setTips(data.tips);
  };

  return (
    <div style={{ marginTop: "20px" }}>
      <h2>📌 Study Tips</h2>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Paste your study notes here"
        rows={4}
        cols={50}
      />
      <br />
      <button onClick={getTips}>Generate Tips</button>
      <ul>
        {tips.map((t, i) => (
          <li key={i}>{t}</li>
        ))}
      </ul>
    </div>
  );
}

export default Tips;
