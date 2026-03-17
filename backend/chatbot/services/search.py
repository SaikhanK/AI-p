from product.models import Product
from django.db.models import Q

def search_hardware_db(query: str, max_price: float = None):
    results = Product.objects.filter(
         Q(title__icontains=query)
    )
    
    if max_price:
        results = results.filter(price__lte=max_price)
    
    return [
        {"id": p.id, "name": p.title, "price": str(p.price)} 
        for p in results[:5]
    ]

from langchain_core.messages import HumanMessage, SystemMessage

def extract_data(text_content, llm_instance):
    llm_json = llm_instance.bind(response_format={"type": "json_object"})
    
    system_prompt = "Analysiere den Text und Extrahiere schlüssel Daten als JSON. Antworte NUR im JSON-Format."
    
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"Text: {text_content}")
    ]
    
    response = llm_json.invoke(messages)
    return response.content