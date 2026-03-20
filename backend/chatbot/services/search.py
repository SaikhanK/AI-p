from product.models import Product
from django.db.models import Q
import pandas as pd
from langchain_core.messages import HumanMessage, SystemMessage
import json

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

def search_hardware(parameter: dict) -> pd.DataFrame:
    if isinstance(parameter, str):
        parameter = json.loads(parameter)
    if parameter.get("product_category"):
        results = Product.objects.filter(
            title__icontains=parameter["product_category"]
        )
    else: 
        results = Product.objects.all()
    
    query = Q()

    for key, value in parameter["product_attributes"].items():
        if value:
            query &= Q(
                attributes__attribute__name=key,
                attributes__value__value=value
            )

    results = results.filter(query).distinct()
    raise ValueError(results)
    pass

def extract_data(text_content, llm_instance):
    llm_json = llm_instance.bind(response_format={"type": "json_object"})

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=f"Text: {text_content}")
    ]
    
    response = llm_json.invoke(messages)
    return response.content