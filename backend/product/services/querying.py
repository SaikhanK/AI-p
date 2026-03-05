from ..paramter import QueryParameter
from ..models import Product
import pandas as pd

def generate_dataframe(data: QueryParameter)-> pd.DataFrame:
    query_set = get_query_set(data)
    df = pd.DataFrame(query_set.values('id', 'title', 'price'))
    return df


def get_query_set(data: QueryParameter):
    if data.category:
        query_set = Product.objects.filter(category__name=data.category)
    else:
        query_set = Product.objects.all()
    if data.max_price:
        query_set = query_set.filter(price__lte=data.max_price)
    if data.min_price:
        query_set = query_set.filter(price__gte=data.max_price)
    if data.attribute:
        for key, value in data.attribute.items():
            query_set = query_set.filter(key = value)
    return query_set


