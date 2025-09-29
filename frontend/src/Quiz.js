import { useState } from "react";

function Quiz() {
  const [subject, setSubject] = useState("");
  const [level, setLevel] = useState(1);
  const [quiz, setQuiz] = useState([]);
  const [score, setScore] = useState(0);
  const [answered, setAnswered] = useState(0);

  const getQuiz = async () => {
    setScore(0);
    setAnswered(0);
    const res = await fetch("http://localhost:5000/api/quiz", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ subject, level }),
    });
    const data = await res.json();
    setQuiz(data.quiz);
  };

  const handleAnswer = (selected, correct, i) => {
    if (selected === correct) setScore(prev => prev + 1);
    setAnswered(prev => prev + 1);
  };

  return (
    <div>
      <h2>📝 Quiz</h2>
      <input value={subject} onChange={e => setSubject(e.target.value)} placeholder="Enter subject" />
      <select value={level} onChange={e => setLevel(Number(e.target.value))}>
        <option value={1}>Level 1 (Very Easy)</option>
        <option value={2}>Level 2 (Easy)</option>
        <option value={3}>Level 3 (Medium)</option>
        <option value={4}>Level 4 (Hard)</option>
        <option value={5}>Level 5 (Very Hard)</option>
      </select>
      <button onClick={getQuiz}>Get Quiz</button>

      {quiz.map((q, i) => {
        let opts = [];
        try {
          if (
            q.options !== undefined &&
            q.options !== null &&
            q.options !== "undefined"
          ) {
            opts = JSON.parse(q.options);
          }
        } catch (e) {
          opts = [];
        }
        return (
          <div key={i} style={{ margin: "10px", padding: "10px", border: "1px solid #ccc" }}>
            <p><b>Q{i + 1}:</b> {q.question}</p>
            {opts.map((opt, j) => (
              <button key={j} onClick={() => handleAnswer(opt, q.answer, i)} disabled={answered > i}>
                {opt}
              </button>
            ))}
          </div>
        );
      })}

      {answered === quiz.length && quiz.length > 0 && (
        <h3>✅ You scored {score}/{quiz.length}</h3>
      )}
    </div>
  );
}

export default Quiz;
