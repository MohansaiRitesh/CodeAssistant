# =============================================================
# The Chat Interface
# =============================================================

from agent import create_agent, chat


# Welcome banner
BANNER = """
╔══════════════════════════════════════════════════════════════╗
║           🤖  AI Code Assistant  (Powered by LangChain)     ║
╠══════════════════════════════════════════════════════════════╣
║  What I can do:                                              ║
║  ✅  Write code in any language                              ║
║  ✅  Debug your errors                                       ║
║  ✅  Explain what code does                                  ║
║  ✅  Teach programming concepts                              ║
║  ✅  Review and improve your code                            ║
╠══════════════════════════════════════════════════════════════╣
║  Commands:                                                   ║
║  Type 'quit' or 'exit' to stop                               ║
║  Type 'clear' to start a fresh conversation                  ║
║  Type 'help' to see example questions                        ║
╚══════════════════════════════════════════════════════════════╝
"""

HELP_TEXT = """
📚 Example questions you can ask me:

  WRITE CODE:
  → "Write a Python function that checks if a number is prime"
  → "Create a JavaScript function to reverse a string"
  → "Build a simple to-do list class in Python"

  DEBUG:
  → "I get this error: TypeError: 'int' object is not iterable"
  → "My code doesn't work: [paste your broken code]"
  → "Fix this: for i in range(5): print(i[0])"

  EXPLAIN:
  → "Explain what this does: [paste code]"
  → "What does *args mean in Python?"
  → "Walk me through how recursion works"

  LEARN CONCEPTS:
  → "What is a REST API?"
  → "Explain object-oriented programming"
  → "What's the difference between a list and a tuple?"

  REVIEW:
  → "Review my code: [paste code]"
  → "How can I improve this function?"
"""


# Main chat loop
def main():
    print(BANNER)
    
    # Initialize the agent
    # This creates the LLM + prompt + tools + memory all at once
    print("⚡ Starting up your AI Code Assistant...")
    print("   (Using Groq's free API with Llama 3.1 — very fast!)\n")
    
    try:
        agent = create_agent()
        print("✅ Agent ready! Start asking coding questions.\n")
    except Exception as e:
        print(f"❌ Failed to start: {e}")
        print("👉 Make sure you set GROQ_API_KEY in your .env file")
        print("   Get a free key at: https://console.groq.com")
        return
    
    # ---------------------------------------------------------------
    # CONCEPT: The Agentic Loop
    # This while loop is where the "agentic" behavior happens.
    # We keep asking questions, and the agent:
    # 1. Reads the question
    # 2. Decides what tool to call
    # 3. Calls the tool
    # 4. Uses the tool's output to form a final answer
    # 5. Returns the answer (with memory of everything so far)
    # ---------------------------------------------------------------
    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()
            
            # Handle special commands
            if not user_input:
                continue
            
            if user_input.lower() in ["quit", "exit", "q"]:
                print("\n👋 Goodbye! Keep coding! 🚀")
                break
            
            if user_input.lower() == "help":
                print(HELP_TEXT)
                continue
            
            if user_input.lower() == "clear":
                # Restart the agent with fresh memory
                agent = create_agent()
                print("🔄 Conversation cleared! Fresh start.\n")
                continue
            
            # Send the message to the agent and get a response
            print("\n🤔 Thinking...\n")
            print("-" * 60)
            
            # CONCEPT: This single line does A LOT:
            # 1. Formats the prompt with chat history + current input
            # 2. Sends to Groq LLM
            # 3. LLM picks a tool
            # 4. Tool runs and returns output
            # 5. LLM sees tool output and writes final answer
            # 6. Answer + conversation saved to memory
            response = chat(agent, user_input)
            
            print("-" * 60)
            print(f"\n🤖 Assistant:\n{response}\n")
        
        except KeyboardInterrupt:
            print("\n\n👋 Interrupted. Goodbye!")
            break
        
        except Exception as e:
            print(f"\n⚠️  Error: {e}\n")
            continue


if __name__ == "__main__":
    main()
