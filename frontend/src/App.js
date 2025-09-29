import './App.css';
import { useState } from 'react';
import StudyPlan from './StudyPlan';
import Quiz from './Quiz';
import Summarizer from './Summarizer';
import Tips from './Tips';
import Feedback from './Feedback';

function App() {
  const [view, setView] = useState('home');

  return (
    <div className="App">
      <header className="App-header">
        <h1>AI Study Pal</h1>
        <nav style={{ marginTop: 12 }}>
          <button onClick={() => setView('study')}>Study Plan</button>
          <button onClick={() => setView('quiz')}>Quiz</button>
          <button onClick={() => setView('summ')}>Summarizer</button>
          <button onClick={() => setView('tips')}>Tips</button>
          <button onClick={() => setView('feedback')}>Feedback</button>
        </nav>
      </header>

      <main style={{ padding: 16 }}>
        {view === 'home' && (
          <div>
            <h2>Welcome to AI Study Pal</h2>
            <p>Choose a tool above to get started.</p>
          </div>
        )}
        {view === 'study' && <StudyPlan />}
        {view === 'quiz' && <Quiz />}
        {view === 'summ' && <Summarizer />}
        {view === 'tips' && <Tips />}
        {view === 'feedback' && <Feedback />}
      </main>
    </div>
  );
}

export default App;
