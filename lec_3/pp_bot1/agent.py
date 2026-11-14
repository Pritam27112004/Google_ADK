#performing google search  Q:tell me top 10 ai news
# from google.adk.agents.llm_agent import Agent
# from google.adk.tools.google_search_tool import google_search

# root_agent = Agent(
#     model='gemini-3.5-flash',
#     name='root_agent',
#     description="A helpful assistant that can search the web.",
#     instruction=(
#         "Answer user questions accurately. "
#         "Use Google Search when you need current information "
#         "or need to verify facts."
#     ),
#     tools=[google_search],
# )


#code execution agent Q: give data and ask data analysis , the agent will run python code , get result and return you
from google.adk.agents.llm_agent import Agent
from google.adk.code_executors import BuiltInCodeExecutor

root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description="A helpful assistant that can write and run Python code.",
    instruction=(
        "Answer user questions accurately. "
        "When a question involves calculations, data analysis, or anything "
        "that benefits from running code, write Python and execute it, "
        "then explain the result."
    ),
    code_executor=BuiltInCodeExecutor(),
)