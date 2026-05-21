import { useState } from "react";

function App() {

  const [query, setQuery] = useState("");
  const [logs, setLogs] = useState("");
  const [loading, setLoading] = useState(false);

  const startPipeline = async () => {

    setLogs("");
    setLoading(true);

    const response = await fetch(
      `http://127.0.0.1:8000/process?query=${query}`,
      {
        method: "POST"
      }
    );

    const reader = response.body.getReader();

    const decoder = new TextDecoder();

    while (true) {

      const { done, value } = await reader.read();

      if (done) break;

      const chunk = decoder.decode(value);

      setLogs(prev => prev + chunk);
    }

    setLoading(false);
  };

  return (
    <div
      style={{
        minHeight: "100vh",
        background: "#0f172a",
        color: "white",
        padding: "40px",
        fontFamily: "Arial"
      }}
    >

      {/* HEADER */}

      <div
        style={{
          textAlign: "center",
          marginBottom: "40px"
        }}
      >
        <h1
          style={{
            fontSize: "48px",
            marginBottom: "10px"
          }}
        >
          Agentic AI System
        </h1>

        <p
          style={{
            color: "#94a3b8",
            fontSize: "18px"
          }}
        >
          Multi-Agent Distributed AI Pipeline
        </p>
      </div>

      {/* INPUT SECTION */}

      <div
        style={{
          display: "flex",
          justifyContent: "center",
          gap: "10px",
          marginBottom: "30px"
        }}
      >

        <input
          type="text"
          placeholder="Enter your query..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          style={{
            width: "500px",
            padding: "15px",
            borderRadius: "10px",
            border: "none",
            outline: "none",
            fontSize: "16px",
            background: "#1e293b",
            color: "white"
          }}
        />

        <button
          onClick={startPipeline}
          disabled={loading}
          style={{
            padding: "15px 25px",
            borderRadius: "10px",
            border: "none",
            background: loading ? "#475569" : "#3b82f6",
            color: "white",
            cursor: "pointer",
            fontSize: "16px",
            fontWeight: "bold"
          }}
        >
          {loading ? "Running..." : "Run Agents"}
        </button>

      </div>

      {/* AGENT STATUS CARDS */}

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(4, 1fr)",
          gap: "20px",
          marginBottom: "30px"
        }}
      >

        {[
          "Planner",
          "Retriever",
          "Analyzer",
          "Writer"
        ].map((agent) => (

          <div
            key={agent}
            style={{
              background: "#1e293b",
              padding: "20px",
              borderRadius: "15px",
              textAlign: "center",
              boxShadow: "0 4px 20px rgba(0,0,0,0.3)"
            }}
          >

            <h3>{agent} Agent</h3>

            <div
              style={{
                marginTop: "15px",
                width: "12px",
                height: "12px",
                borderRadius: "50%",
                background: "#22c55e",
                marginInline: "auto"
              }}
            />

          </div>
        ))}

      </div>

      {/* LOG TERMINAL */}

      <div
        style={{
          background: "#020617",
          borderRadius: "15px",
          padding: "25px",
          height: "450px",
          overflowY: "scroll",
          border: "1px solid #334155",
          boxShadow: "0 4px 20px rgba(0,0,0,0.4)"
        }}
      >

        <div
          style={{
            marginBottom: "15px",
            color: "#38bdf8",
            fontWeight: "bold"
          }}
        >
          LIVE PIPELINE LOGS
        </div>

        <pre
          style={{
            color: "#22c55e",
            whiteSpace: "pre-wrap",
            fontSize: "15px",
            lineHeight: "1.6"
          }}
        >
          {logs || "Waiting for query..."}
        </pre>

      </div>

    </div>
  );
}

export default App;