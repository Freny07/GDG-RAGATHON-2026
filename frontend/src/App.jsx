import { useState } from "react";
import axios from "axios";

export default function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [simulateResult, setSimulateResult] = useState(null);

  const handlePredict = async () => {
    const res = await axios.post("http://127.0.0.1:8000/predict", {
      text,
      role: "SDE",
    });
    setResult(res.data);
  };

  const handleSimulate = async () => {
    const res = await axios.post("http://127.0.0.1:8000/simulate", {
      text,
      changes: {
        projects: 3,
        experience: 2,
        dsa: 7,
      },
    });
    setSimulateResult(res.data);
  };

  return (
    <div className="min-h-screen bg-black text-white p-6">
      <h1 className="text-4xl font-bold text-center mb-6">
        🚀 Placement Predictor
      </h1>

      {/* INPUT */}
      <textarea
        className="w-full p-4 rounded-lg bg-gray-900"
        rows="5"
        placeholder="Paste your resume or profile..."
        onChange={(e) => setText(e.target.value)}
      />

      {/* BUTTONS */}
      <div className="flex gap-4 mt-4">
        <button
          onClick={handlePredict}
          className="bg-blue-500 px-4 py-2 rounded-lg hover:bg-blue-600"
        >
          Predict
        </button>

        <button
          onClick={handleSimulate}
          className="bg-purple-500 px-4 py-2 rounded-lg hover:bg-purple-600"
        >
          Simulate 🚀
        </button>
      </div>

      {/* RESULT */}
      {result && (
        <div className="mt-6 bg-gray-900 p-4 rounded-lg">
          <h2 className="text-xl font-bold">Score: {result.score}</h2>
          <p>Level: {result.level}</p>
          <p>Profile: {result.profile_type}</p>
          <p>Confidence: {result.confidence}</p>

          <h3 className="mt-3 font-bold">Skill Gaps:</h3>
          <ul>
            {result.skill_gaps.map((g, i) => (
              <li key={i}>• {g}</li>
            ))}
          </ul>

          <h3 className="mt-3 font-bold">Roadmap:</h3>
          <ul>
            {result.roadmap.map((r, i) => (
              <li key={i}>• {r}</li>
            ))}
          </ul>
        </div>
      )}

      {/* SIMULATION */}
      {simulateResult && (
        <div className="mt-6 bg-purple-900 p-4 rounded-lg">
          <h2 className="text-xl font-bold">
            Improved Score: {simulateResult.improved_score}
          </h2>
          <p>Impact: +{simulateResult.impact}</p>
          <p>{simulateResult.message}</p>
        </div>
      )}
    </div>
  );
}