from product.models import Product
from django.db.models import Q
import json

KNOWN_BRANDS = ["apple", "samsung", "sony", "dell", "hp", "lenovo", "asus", "acer", "microsoft", "huawei", "lg", "nvidia", "amd", "intel"]

CATEGORY_SYNONYMS = {
    "handy": "smartphones",
    "handys": "smartphones",
    "mobiltelefon": "smartphones",
    "telefon": "smartphones",
    "phone": "smartphones",
    "notebook": "laptops",
    "notebooks": "laptops",
    "rechner": "pc",
    "computer": "pc",
    "grafikkarte": "gpu",
    "prozessor": "cpu",
    "hauptspeicher": "ram",
    "festplatte": "ssd",
}


def _resolve_query(query: str):
    """
    Gibt (category, brand) zurück.
    - Wenn query eine bekannte Marke ist -> category=None, brand=query
    - Wenn query ein Synonym hat -> category=normalisierter Begriff
    - Sonst -> category=query, brand=None
    """
    q = query.strip().lower()

    if q in KNOWN_BRANDS:
        return None, q.capitalize()

    resolved = CATEGORY_SYNONYMS.get(q, q)
    return resolved, None


def search_hardware_complex(parameter: dict):
    """
    Sucht Produkte basierend auf Kategorie, Preis und Attributen.
    Unterstützt Marken-Suche und Synonym-Auflösung.
    """
    if isinstance(parameter, str):
        try:
            parameter = json.loads(parameter)
        except Exception:
            return []

    results = Product.objects.all()

    category = parameter.get("product_category")
    if category:
        resolved_category, resolved_brand = _resolve_query(category)

        if resolved_brand:
            results = results.filter(
                Q(title__icontains=resolved_brand) |
                Q(attributes__value__value__icontains=resolved_brand)
            ).distinct()
        elif resolved_category:
            results = results.filter(
                Q(title__icontains=resolved_category) |
                Q(category__name__icontains=resolved_category)
            )
            
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