# =============================================================
# The Agent's Toolbox
# =============================================================
# CONCEPT: Tools are Python functions that your AI agent can CHOOSE to call.
# The agent reads the function name and docstring to decide when to use each one.
# Think of it as giving the AI a menu of capabilities.
#
# LangChain uses the @tool decorator to turn a regular Python function
# into something the agent can discover and call automatically.
# =============================================================

from langchain_core.tools import tool


# TOOL 1: Write Code

# The @tool decorator is the key concept here.
# It tells LangChain: "This function is a tool the agent can use."
# The docstring (the text in triple quotes) is VERY IMPORTANT —
# the LLM reads it to know WHEN to use this tool.
@tool
def write_code(request: str) -> str:
    """
    Use this tool when the user asks you to WRITE, CREATE, or GENERATE code.
    Input: A description of what code to write, including the programming language.
    Output: Clean, well-commented code with an explanation.
    Examples: 'write a Python function to sort a list', 'create a JavaScript counter'
    """
    # This tool returns a prompt that guides the LLM to generate code.
    # The agent passes this result back to the LLM for the final answer.
    return f"""
    You are an expert coding assistant. The user wants you to write code for:
    
    REQUEST: {request}
    
    Please provide:
    1. The complete, working code
    2. Inline comments explaining each important line
    3. A brief explanation of HOW the code works
    4. An example of how to USE the code
    
    Make the code beginner-friendly with clear variable names.
    """


# TOOL 2: Debug Code
@tool
def debug_code(error_and_code: str) -> str:
    """
    Use this tool when the user has an ERROR, BUG, or code that is NOT WORKING.
    Input: The error message AND/OR the broken code (paste both together).
    Output: An explanation of the bug and the fixed code.
    Examples: 'IndexError: list index out of range', 'my for loop gives wrong answer'
    """
    return f"""
    You are an expert debugger. Analyze this error/broken code:
    
    {error_and_code}
    
    Please provide:
    1. WHAT is the bug? (explain in simple terms)
    2. WHY does this error happen? (root cause)
    3. HOW to fix it? (show the corrected code)
    4. HOW to avoid this bug in the future? (1-2 tips)
    
    Be encouraging — bugs happen to every programmer!
    """


# TOOL 3: Explain Code
@tool
def explain_code(code: str) -> str:
    """
    Use this tool when the user wants to UNDERSTAND, EXPLAIN, or LEARN what code does.
    Input: The code snippet the user wants explained.
    Output: A step-by-step plain-English explanation.
    Examples: 'explain this function', 'what does this code do', 'break this down for me'
    """
    return f"""
    You are a patient coding teacher. Explain this code to a beginner:
    
    {code}
    
    Please provide:
    1. A one-sentence summary of what this code does overall
    2. A line-by-line breakdown (explain each part in simple English)
    3. Any important concepts used (e.g., loops, functions, recursion)
    4. A real-world analogy to help it click
    
    Avoid jargon. Imagine you're explaining to someone on their first week of coding.
    """


# TOOL 4: Search Programming Concepts
@tool
def search_concept(concept: str) -> str:
    """
    Use this tool when the user asks WHAT something is, or wants to LEARN a concept.
    Input: A programming concept, term, or technology name.
    Output: A clear explanation with examples.
    Examples: 'what is recursion', 'explain APIs', 'what does async/await mean'
    """
    return f"""
    You are a knowledgeable programming teacher. Explain this concept clearly:
    
    CONCEPT: {concept}
    
    Please provide:
    1. A simple definition (1-2 sentences, no jargon)
    2. WHY it exists / what problem it solves
    3. A simple code example showing it in action
    4. Common use cases (when do real developers use this?)
    5. One common beginner mistake to avoid
    
    Use analogies from everyday life to make it memorable.
    """


# TOOL 5: Review and Improve Code
@tool
def review_code(code: str) -> str:
    """
    Use this tool when the user wants their code REVIEWED, IMPROVED, OPTIMIZED, or wants FEEDBACK.
    Input: The code the user wants reviewed.
    Output: Specific feedback and an improved version.
    Examples: 'review my code', 'make this faster', 'is my code good?', 'improve this'
    """
    return f"""
    You are a senior developer doing a friendly code review. Review this code:
    
    {code}
    
    Please provide:
    1. What's GOOD about this code (always start positive!)
    2. What could be IMPROVED (be specific, not vague)
    3. Any potential BUGS or edge cases missed
    4. The IMPROVED version of the code
    5. Key LESSONS from this review (1-2 things to remember)
    
    Be constructive and encouraging. The goal is to help them grow.
    """


# Collect all tools in a list so we can easily pass them to the agent later. The agent will have access to ALL of these capabilities.
ALL_TOOLS = [
    write_code,
    debug_code,
    explain_code,
    search_concept,
    review_code,
]
