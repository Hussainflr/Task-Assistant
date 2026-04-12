# 🧠 Multi-Agent Task Assistant with local LLM  (Streamlit + AutoGen + Ollama)

A clean, modular **multi-agent AI application** that plans, executes, and generates responses using local LLMs.
Built for learning and experimentation with **agent orchestration, memory, and tool usage**.

---

## 🚀 Features

* 🤖 Multi-agent system (Planner → Worker → Writer)
* ⚡ Fast mode (single-agent for simple tasks)
* 🧠 Short-term + long-term memory (ChromaDB)
* 🔧 Tool integration (search + calculator)
* 🖥️ Streamlit UI with logs and outputs
* ⚙️ YAML-based configuration (no hardcoding)
* 🧩 Modular and extensible architecture

---

## 🏗️ Architecture

```
User Input
   ↓
[Fast Mode?] ── Yes → Single Agent → Output
   ↓ No
Planner Agent
   ↓
Worker Agent (tools + execution)
   ↓
Writer Agent
   ↓
Memory Store (ChromaDB)
   ↓
Final Output
```

---

## 📁 Project Structure

```
multi_agent_app/
│
├── app.py                     # Streamlit UI
│
├── config/
│   ├── config.yaml           # All configs (LLM, agents, memory, prompts)
│   └── config_loader.py      # Global config access
│
├── agents/
│   ├── planner.py
│   ├── worker.py
│   └── writer.py
│
├── core/
│   └── orchestrator.py       # Main logic (agent flow)
│
├── memory/
│   ├── short_term.py
│   └── long_term.py
│
├── tools/
│   ├── search.py
│   ├── calculator.py
│   └── tool_registry.py
│
├── utils/
│   ├── logger.py
│   └── prompt_builder.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repo

```
git clone <your-repo-url>
cd multi_agent_app
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Install & run Ollama

Install:

```
brew install ollama
```

Run server:

```
ollama serve
```

Pull model:

```
ollama pull qwen3:4b
```

---

## ▶️ Run the App

```
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🧪 Example Usage

Try inputs like:

* "Create a 7-day study plan for Python basics"
* "Plan a 2-day trip to Karachi"
* "Calculate 25 * 40"

---

## 🧠 Memory System

### Short-Term Memory

* Keeps recent conversation (buffer)
* Stored in session

### Long-Term Memory

* Stored in ChromaDB
* Retrieves relevant past outputs

---

## 🔧 Tools

* 🔍 Search Tool (mock / extendable)
* 🧮 Calculator Tool (real execution)

---

## ⚡ Fast Mode

For simple tasks, system skips multi-agent flow:

```
User → Single LLM → Output
```

Controlled via:

```yaml
performance:
  fast_mode: true
```

---

## ⚙️ Configuration

All settings are controlled via:

📁 `config/config.yaml`

Examples:

```yaml
llm:
  model: qwen:1.8b

agents:
  planner:
    max_turns: 1

performance:
  fast_mode: true
```

<!-- ---

## 🧩 Prompt System

Prompts are configurable:

```yaml
prompts:
  planner: |
    Context:
    {context}

    Task:
    {task}
```

--- -->

## 🐞 Debugging

Enable debug logs:

```yaml
debug:
  verbose_logs: true
  print_chat_history: true
```

---

## ⚠️ Common Issues

### Slow response

* Use smaller model (`qwen:1.8b`)
* Enable fast mode
* Reduce agent calls

---

### ChromaDB errors

```
pip install -U chromadb pydantic-settings
```

---

### Ollama not responding

```
ollama serve
```

---

## 🚀 Future Improvements

* 🎤 Voice input/output
* 🌐 Real search API
* 📂 File upload + RAG
* 🔁 Streaming responses
* 🧠 Smarter memory retrieval
* 🤝 GroupChat agents

---

## 🔑 Key Learnings

* Multi-agent systems add power but also complexity
* Memory and orchestration matter more than model size
* Fast routing is essential for performance

---

## 📜 License

MIT License

---

## 🙌 Acknowledgements

* AutoGen for multi-agent framework
* Ollama for local LLM execution
* Streamlit for rapid UI development

---

## 💡 Final Note

This project is designed to help you **understand agentic AI systems deeply**—not just use them.

Start simple → then scale.

---
