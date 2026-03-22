from product.models import Product
from django.db.models import Q
import json
from langchain_core.messages import HumanMessage, SystemMessage

SYSTEM_PROMPT = """
Du bist ein Daten-Extraktor für einen Hardware-Shop. Deine Aufgabe ist es, Kundenanfragen zu analysieren und strukturierte Daten im JSON-Format zurückzugeben.

Extrahiere folgende Felder:
- product_category: Die Art des Produkts (z.B. Laptops, Grafikkarten, CPU).
- amount: Die gewünschte Anzahl als Ganzzahl (Default: 1).
- price_limit: Das maximale Budget pro Stück, falls erwähnt (sonst null).
- product_attributes: Ein Dictionary mit technischen Details (z.B. {"ram": "16GB", "storage": "512GB", "color": "Black", "brand": "Apple"}).

Regeln:
1. Antworte NUR mit dem JSON-Objekt.
2. Wenn Informationen fehlen, setze den Wert auf null.
3. Erfinde keine Daten, die nicht im Text stehen.
"""

def search_hardware_complex(parameter: dict):
    """
    Sucht Produkte basierend auf Kategorie, Preis und technischen Attributen.
    """
    if isinstance(parameter, str):
        try:
            parameter = json.loads(parameter)
        except:
            return []

    results = Product.objects.all()

    category = parameter.get("product_category")
    if category:
        results = results.filter(
            Q(title__icontains=category) | Q(category__name__icontains=category)
        )

    price_limit = parameter.get("price_limit")
    if price_limit:
        results = results.filter(price__lte=float(price_limit))

    attributes = parameter.get("product_attributes", {})
    if attributes and isinstance(attributes, dict):
        for key, value in attributes.items():
            if value:
                results = results.filter(
                    attributes__attribute__name__iexact=key,
                    attributes__value__value__iexact=str(value)
                ).distinct()

    return [
        {"id": p.id, "name": p.title, "price": f"{p.price}€"} 
        for p in results[:5]
    ]

def extract_data(text_content, llm_instance):
    """Nutzt das LLM, um strukturierte Daten aus dem User-Text zu ziehen."""
    llm_json = llm_instance.bind(response_format={"type": "json_object"})
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=f"Text: {text_content}")
    ]
    response = llm_json.invoke(messages)
    return json.loads(response.content)

def extract_data_with_context(user_input, chat_history, llm_instance):
    """
    Analysiert die aktuelle Anfrage unter Berücksichtigung des bisherigen Gesprächs.
    """
    llm_json = llm_instance.bind(response_format={"type": "json_object"})
    
    messages = [SystemMessage(content=SYSTEM_PROMPT)] 
    
    for msg in chat_history[-4:]: 
        messages.append(msg)
        
    messages.append(HumanMessage(content=f"Aktuelle User-Anfrage: {user_input}"))
    
    response = llm_json.invoke(messages)
    return json.loads(response.content)