from ..paramter import QueryParameter
from ..models import Product
import pandas as pd

def generate_dataframe(data: QueryParameter)-> pd.DataFrame:
    query_set = get_query_set(data)
    df = pd.DataFrame(query_set.values('id', 'title', 'price'))
    return df


def get_query_set(data: QueryParameter):
    if data.product_category:
        query_set = Product.objects.filter(category__name=data.product_category)
    else:
        query_set = Product.objects.all()
    if data.product_brand:
        query_set = query_set.filter(attributes__value__value__icontains=data.product_brand)
    return query_set


