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