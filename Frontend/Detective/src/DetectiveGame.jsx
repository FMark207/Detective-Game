import React, { useEffect, useState } from "react";
import axios from "axios";
import "./DetectiveGame.css";

export default function DetectiveGame() {
  const [suspects, setSuspects] = useState([]);
  const [traits, setTraits] = useState([]);
  const [statements, setStatements] = useState([]);
  const [murderStats, setMurderStats] = useState(null);
  const [selectedSuspect, setSelectedSuspect] = useState(null);
  const [guess, setGuess] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadData() {
      try {
        const [susRes, traitsRes, stmtRes, murderRes] = await Promise.all([
          axios.get("/api/suspects/"),
          axios.get("/api/suspect-traits/"),
          axios.get("/api/statements/"),
          axios.get("/api/murder-stats/"),
        ]);

        setSuspects(susRes.data);
        setTraits(traitsRes.data);
        setStatements(stmtRes.data);
        setMurderStats(murderRes.data[0]);
      } catch (err) {
        console.error("❌ Failed to load data:", err);
      } finally {
        setLoading(false);
      }
    }

    loadData();
  }, []);

  const getTraitsByName = (name) =>
    traits.filter((t) => t.suspect === name).map((t) => t.trait);

  const getStatementsByName = (name) =>
    statements.filter((s) => s.suspect === name);

  const handleSelect = (suspect) => {
    setSelectedSuspect(suspect);
  };

  const handleGuess = (suspectId) => {
    const actualTraitor = suspects.find((s) => s.isMurder);
    setGuess({
      chosen: suspects.find((s) => s.id === suspectId),
      correct: actualTraitor,
      result: suspectId === actualTraitor.id,
    });
  };

  if (loading) return <div className="container">Loading game data...</div>;

  return (
    <div className="container">
      <h1>🕵️ Detective Game</h1>
      <p className="subheading">Investigate suspects and find the traitor.</p>

      {murderStats && (
        <div className="clue-box">
          <p>
            <strong>Weapon:</strong> {murderStats.murderWeapon}
          </p>
          <p>
            <strong>Time:</strong> {murderStats.murderTime}
          </p>
          <p>
            <strong>Clue:</strong> {murderStats.murderNotice}
          </p>
        </div>
      )}

      <div className="suspect-grid">
        {suspects.map((suspect) => (
          <button
            key={suspect.id}
            onClick={() => handleSelect(suspect)}
            className="suspect-card"
          >
            <div className="font-bold">{suspect.name}</div>
            <div className="text-sm">Click to investigate</div>
          </button>
        ))}
      </div>

      {selectedSuspect && (
        <div className="investigation-panel">
          <h2>🧍 Investigating: {selectedSuspect.name}</h2>

          <div className="mb-4">
            <h3>Traits:</h3>
            <ul>
              {getTraitsByName(selectedSuspect.name).map((trait, index) => (
                <li key={index}>{trait}</li>
              ))}
            </ul>
          </div>

          <div>
            <h3>Statements:</h3>
            <ul>
              {getStatementsByName(selectedSuspect.name).map((s) => (
                <li key={s.id}>
                  <strong>{s.detective}:</strong> <q>{s.statement_text}</q>
                </li>
              ))}
            </ul>
          </div>

          <button
            onClick={() => handleGuess(selectedSuspect.id)}
            className="guess-button"
          >
            I think this is the traitor!
          </button>
        </div>
      )}

      {guess && (
        <div className="result-panel">
          <h2>
            {guess.result ? "✅ You found the traitor!" : "❌ Wrong guess!"}
          </h2>
          <p>
            You guessed: <strong>{guess.chosen.name}</strong>
          </p>
          <p>
            The actual traitor was: <strong>{guess.correct.name}</strong>
          </p>
        </div>
      )}
    </div>
  );
}
