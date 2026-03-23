from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from langchain_groq import ChatGroq
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool
from product.models import Product
from product.serializers import ProductChatSerializer
import re

from chatbot.services.search import search_hardware_complex
from chatbot.parameter import QueryParameter


@tool
def hardware_search_tool(query: str):
    """
    Sucht passende Hardware in der Datenbank.
    Eingabe 'query' sollte ein einfacher Suchbegriff sein (z.B. 'MacBook' oder 'Gaming PC').
    """
    search_params = {
        "product_category": query,
        "product_attributes": {}
    }
    return search_hardware_complex(search_params)


tools = [hardware_search_tool]

llm = ChatGroq(
    temperature=0,
    groq_api_key="",
    model_name="llama-3.1-8b-instant"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", """Du bist ein freundlicher IT-Hardware-Verkäufer.
    REGELN:
    1. Nutze IMMER zuerst das Tool 'hardware_search_tool', um nach echten Produkten zu suchen.
    2. Nenne NIEMALS Produkte, die nicht in den Ergebnissen des Tools auftauchen.
    3. Wenn das Tool keine Ergebnisse liefert, sage dem Kunden höflich, dass das gewünschte Produkt aktuell nicht vorrätig ist.
    4. Beende deine Antwort IMMER mit der ID des Produkts im Format: [ID: 123].
    5. Wenn kein Produkt gefunden wurde, schreibe [ID: None]."""),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


class ModelView(GenericViewSet):

    def chat(self, request):
        serializer = QueryParameter(**request.query_params.dict())
        user_input = serializer.user_input

        if not user_input:
            return Response({"error": "user_input is required."}, status=400)

        try:
            response = agent_executor.invoke({"input": user_input})
            output_text = response["output"]

            product_ids = re.findall(r"\[ID:\s*(\d+)\]", output_text)
            products = Product.objects.filter(id__in=product_ids)
            serialized_products = ProductChatSerializer(products, many=True).data

            return Response({
                "answer": output_text,
                "recommended_products": serialized_products
            })

        except Exception as e:
            return Response({"error": str(e)}, status=500)