# 🤖 Agentic AI Code Assistant

> A fully agentic AI-powered code assistant built with **LangChain** + **Groq** (free tier).  
> Runs in your terminal — writes, debugs, explains, and reviews code in any language.

---

## ✨ Features

| Capability | Description |
|---|---|
| ✅ Write Code | Generate clean, commented code in any language |
| ✅ Debug Errors | Paste your error — get the fix + explanation |
| ✅ Explain Code | Line-by-line plain-English breakdown |
| ✅ Learn Concepts | Understand programming concepts with examples |
| ✅ Review Code | Get feedback and an improved version |
| ✅ Memory | Remembers your full conversation context |

---

## 🧠 LangChain Concepts Covered

This project is built to **teach LangChain from scratch** — every file is heavily commented explaining each concept as you read it.

```
Concept                What it does in this project
──────────────────────────────────────────────────────
LLM (ChatGroq)         The AI brain — Llama 3.3 running on Groq's free API
Prompt Template        Reusable system instructions with {variables}
Tools (@tool)          Python functions the agent autonomously picks and calls
Agent                  The decision-maker — reads intent, picks the right tool
AgentExecutor          Runs the tool-calling loop until a final answer is ready
Memory                 Stores the last 10 conversation turns (ConversationBufferWindowMemory)
```

---

## 🗂️ Project Structure

```
code_assistant/
├── .env              
├── .gitignore        
├── requirements.txt  
├── tools.py           5 tools the agent can call
├── agent.py           LLM + Agent + Memory setup
├── app.py             Terminal chat interface
└── README.md          
```

---

## ⚡ Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/code-assistant-agent.git
cd code-assistant-agent
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Get your free Groq API key
1. Go to [console.groq.com](https://console.groq.com)
2. Sign up — **completely free, no credit card needed**
3. Click **API Keys** → **Create API Key**
4. Copy the key

### 4. Set up your `.env` file
```bash
# Create a .env file in the project root
echo "GROQ_API_KEY=your_key_here" > .env
```

### 5. Run it!
```bash
python app.py
```

---

## 💬 Usage Examples

```
You: Write a Python function to check if a number is prime
You: java code for two sum problem
You: I get this error: TypeError: 'int' object is not iterable
You: Explain what recursion is with an example
You: What is the difference between a list and a tuple?
You: Review my code: def add(a,b): return a+b
```

**Commands inside the app:**
```
help     → Show example questions
clear    → Reset the conversation (fresh memory)
quit     → Exit
```

---

## 🏗️ How It Works

```
You type a question
        ↓
Agent reads your intent
        ↓
Agent picks the right tool:
  ├── write_code     → for code generation requests
  ├── debug_code     → for errors and bugs
  ├── explain_code   → for "what does this do"
  ├── search_concept → for "what is X" questions
  └── review_code    → for code feedback
        ↓
Tool calls the LLM with a specialized prompt
        ↓
Response returned + saved to memory
        ↓
You see the answer
```

The agent is **agentic** because it autonomously decides *which tool to use* based on your input — you never have to specify it.

---

## 🛠️ Tech Stack

| Tool | Purpose | Cost |
|---|---|---|
| [LangChain](https://python.langchain.com/) | Agent framework | Free |
| [Groq](https://console.groq.com/) | LLM API (Llama 3.3 70b) | Free tier |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Load `.env` secrets | Free |

---

## 📦 Requirements

```
langchain==0.3.25
langchain-groq==0.3.2
langchain-community==0.3.24
python-dotenv==1.0.1
```

Python **3.9+** recommended.

---

## 🔐 Environment Variables

| Variable | Description |
|---|---|
| `GROQ_API_KEY` | Your Groq API key from [console.groq.com](https://console.groq.com) |

> ⚠️ **Never commit your `.env` file.** It's already listed in `.gitignore`.

---

## 🚀 Next Steps / Ideas

- [ ] Add a web UI with Flask or Streamlit
- [ ] Add a tool that reads your local code files
- [ ] Add RAG — let the agent search programming docs
- [ ] Deploy to Hugging Face Spaces (free hosting)
- [ ] Add a tool that runs code and returns the output

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## 🙏 Acknowledgements

- [LangChain](https://python.langchain.com/) for the agent framework
- [Groq](https://groq.com/) for the blazing-fast free LLM API
- [Meta](https://ai.meta.com/) for the open-source Llama 3.3 model
