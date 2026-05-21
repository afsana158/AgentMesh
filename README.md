# AgentMesh

A distributed multi-agent AI orchestration system built using FastAPI, Redis, React, and asynchronous pipelines.

## Features

- Multi-Agent Architecture
- Distributed Task Queues
- Real-Time Streaming Logs
- Async Processing Pipeline
- Fault Tolerance & Retry Mechanism
- Redis Pub/Sub Communication
- Live Frontend Dashboard
- Scalable Microservice-Like Design

---

# System Architecture

```text
User Query
    ↓
Planner Agent
    ↓
Retriever Queue
    ↓
Retriever Agent
    ↓
Analyzer Queue
    ↓
Analyzer Agent
    ↓
Writer Queue
    ↓
Writer Agent
    ↓
Live Streaming Response
```

---

# Tech Stack

## Backend
- FastAPI
- Python Asyncio
- Redis
- Redis Pub/Sub

## Frontend
- React
- Vite

## Architecture
- Multi-Agent System
- Event-Driven Pipeline
- Distributed Queues
- Streaming Responses

---

# Folder Structure

```text
project/
│
├── agents/
│   ├── planner.py
│   ├── retriever.py
│   ├── analyzer.py
│   └── writer.py
│
├── queue_system/
│   ├── retriever_consumer.py
│   ├── analyzer_consumer.py
│   ├── writer_consumer.py
│   └── pubsub.py
│
├── frontend/
│
├── main.py
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone <your_repo_url>
```

---

# Backend Setup

## Install Dependencies

```bash
pip install fastapi uvicorn redis asyncio
```

## Start Redis

### Mac

```bash
brew services start redis
```

### Docker

```bash
docker run -d -p 6379:6379 redis
```

---

# Run Backend

## Terminal 1

```bash
uvicorn main:app --reload
```

## Terminal 2

```bash
python3 -m queue_system.retriever_consumer
```

## Terminal 3

```bash
python3 -m queue_system.analyzer_consumer
```

## Terminal 4

```bash
python3 -m queue_system.writer_consumer
```

---

# Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at:

```text
http://localhost:5173
```

---

# API Endpoint

## Process Query

```http
POST /process
```

Example:

```text
AI in healthcare
```

---

# Streaming Pipeline

The system streams real-time logs from all agents:

```text
Planner Agent Started...
Retriever Agent Processing...
Analyzer Agent Processing...
Writer Agent Processing...
FINAL OUTPUT...
```

---

# Fault Tolerance

- Retry mechanism implemented
- Queue-based architecture prevents data loss
- Tasks are re-queued on failure

---

# Manual Batching

The system supports manual batching for scalable task processing.

Example:

```python
batch_size = 3
```

---

# Future Improvements

- OpenAI / Ollama Integration
- Docker Deployment
- Kubernetes Scaling
- WebSocket Streaming
- Persistent Database Storage
- Authentication & User Sessions

---

# Author

Soha Afsana
