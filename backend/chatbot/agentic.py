import os
from langchain_groq import ChatGroq
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool

api_key = 'PLACEHOLDER'

llm = ChatGroq(
    temperature=0, 
    groq_api_key="PLACEHOLDER", 
    model_name="llama3-70b-8192"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Du bist ein IT-Hardware-Experte. Nutze das Tool 'hardware_search_tool', um Produkte zu finden. Erstelle daraus ein Angebot."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)