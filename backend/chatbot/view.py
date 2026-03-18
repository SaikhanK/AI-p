
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from langchain_groq import ChatGroq
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool
from rest_framework.response import Response
from chatbot.services.search import search_hardware_db, extract_data
from rest_framework.viewsets import GenericViewSet
from chatbot.parameter import QueryParameter


@tool
def search_hardware_tool(query: str):
    """
    Sucht nach IT-Hardware in der internen Datenbank. 
    Eingabe 'query' muss ein Suchbegriff als String sein (z.B. 'Grafikkarte' oder 'AMD Ryzen').
    Gibt eine Liste mit Produkten, Preisen und Spezifikationen zurück.
    """
    return search_hardware_db(query)

tools = [search_hardware_tool]

llm = ChatGroq(
    temperature=0, 
    groq_api_key="-", 
    model_name="llama-3.1-8b-instant"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", """Du bist ein Hardware-Experte. 
    Wenn du ein passendes Produkt in der Datenbank gefunden hast, nenne es dem User.
    WICHTIG: Beende deine Antwort IMMER mit der ID des ausgewählten Produkts im Format: [ID: 123].
    Wenn kein Produkt passt, schreibe [ID: None]."""),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"), 
])

try:
    agent = create_tool_calling_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
except Exception as e:
    print(f"Fehler bei der Agent-Erstellung: {e}")

class ModelView(GenericViewSet):

    def chat_with_agent(self, request):
        user_input = QueryParameter.model_validate(dict(request.query_params.items()))
        extracted_json = extract_data(user_input, llm)
        
        input_for_agent = f"""
        User-Anfrage: {user_input}
        Extrahierte Daten: {extracted_json}
        Bitte suche passende Produkte und erstelle ein Angebot.
        """
        
        try:
            response = agent_executor.invoke({
                "input": input_for_agent,
                "chat_history": [] 
            })            
            return Response({"output": response["output"]})
        
        except Exception as e:
            return Response({"error": str(e)}, status=500)