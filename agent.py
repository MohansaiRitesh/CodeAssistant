# =============================================================
# The Agent Brain
# =============================================================
# This file wires together all the LangChain concepts:
#   LLM → Prompt Template → Tools → Agent → Memory
# =============================================================


from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.memory import ConversationBufferWindowMemory

from tools import ALL_TOOLS


# Load environment variables
load_dotenv()


# Set up the LLM (the AI model)
def create_llm():
    """Create and return the Groq LLM instance."""
    return ChatGroq(
        model="llama-3.1-8b-instant",           # Fast, free Llama model on Groq
        temperature=0.1,                        # Low = more consistent code answers
        groq_api_key=os.getenv("GROQ_API_KEY")
    )


# Create the Prompt Template

# CONCEPT: Prompt Template
# This is the "system instructions" we give the AI.
# It tells the agent who it is and how to behave.
#
# Special placeholders:
#   {chat_history} — LangChain fills this with past messages (Memory)
#   {input}        — LangChain fills this with the user's current message
#   {agent_scratchpad} — LangChain fills this with the agent's thinking steps

def create_prompt():
    """Create the prompt template for the agent."""
    return ChatPromptTemplate.from_messages([
        # "system" message: instructions that ALWAYS stay at the top
        ("system", """You are an expert coding assistant and patient teacher.

Your personality:
- Friendly, encouraging, and never condescending
- You celebrate when users make progress
- You explain WHY things work, not just HOW

Your capabilities:
- Write clean, well-commented code in any language
- Debug errors with clear explanations
- Explain code in plain English
- Teach programming concepts with examples
- Review and improve existing code

How you work:
- Always use the appropriate tool for each task
- After using a tool, provide a clear, friendly response
- If asked to write code, ALWAYS include comments
- For errors, be encouraging (bugs happen to everyone!)

Remember: You're talking to someone learning to code. Be patient and thorough."""),
        
        # This placeholder is where Memory injects past messages
        # CONCEPT: MessagesPlaceholder lets us inject a list of messages
        #          dynamically. "chat_history" matches our memory's key.
        MessagesPlaceholder(variable_name="chat_history"),
        
        # The user's current message
        ("human", "{input}"),
        
        # This placeholder is where the agent stores its "thinking"
        # (which tools it called, what they returned, etc.)
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])


# Set up Memory

# CONCEPT: Conversation Memory
# Without memory, each message is isolated — the AI forgets everything.
# ConversationBufferWindowMemory keeps the last `k` messages.
#
# Parameters:
#   memory_key: must match the placeholder name in our prompt ("chat_history")
#   k: how many PAIRS of (human + AI) messages to remember
#   return_messages: return as message objects (needed for chat models)
def create_memory():
    """Create conversation memory that remembers the last 10 exchanges."""
    return ConversationBufferWindowMemory(
        memory_key="chat_history",  # Must match MessagesPlaceholder variable name
        k=10,                       # Remember last 10 conversation turns
        return_messages=True        # Return as Message objects, not plain text
    )


# Build the Agent

# CONCEPT: Agent = LLM + Tools + Prompt
# The agent uses the LLM to decide which tool to call,
# calls it, reads the output, and decides what to do next.
# This loop continues until the agent has a final answer.
#
# AgentExecutor is the "runner" that manages this loop.
def create_agent():
    """
    Build and return the complete agent with all components.
    Returns an AgentExecutor ready to chat.
    """
    llm = create_llm()
    prompt = create_prompt()
    memory = create_memory()
    
    # CONCEPT: Tool Binding
    # We tell the LLM about our tools so it knows what's available.
    # The agent will read each tool's name and docstring to decide when to use it.
    agent = create_tool_calling_agent(
        llm=llm,
        tools=ALL_TOOLS,
        prompt=prompt
    )
    
    # CONCEPT: AgentExecutor
    # This is the loop runner. It:
    # 1. Passes input to the agent
    # 2. If agent calls a tool → runs it → feeds result back
    # 3. Repeats until agent gives a final answer
    #
    # Parameters:
    #   verbose=True: prints each step so you can SEE the agent thinking!
    #   max_iterations: safety limit (prevents infinite loops)
    #   handle_parsing_errors: if LLM gives bad output, try again gracefully
    executor = AgentExecutor(
        agent=agent,
        tools=ALL_TOOLS,
        memory=memory,
        verbose=True,             # Show the agent's thinking steps (great for learning!)
        max_iterations=5,         # Max tool calls before giving up
        handle_parsing_errors=True # Gracefully handle LLM output errors
    )
    
    return executor


def chat(agent_executor, user_message: str) -> str:
    """
    Send a message to the agent and get a response.
    
    The agent will:
    1. Read the message
    2. Decide which tool to use (if any)
    3. Call the tool
    4. Generate a final response
    """
    try:
        response = agent_executor.invoke({
            "input": user_message
        })
        # The final answer is in response["output"]
        return response["output"]
    
    except Exception as e:
        return f"Oops! Something went wrong: {str(e)}\nMake sure your GROQ_API_KEY is set in .env"
